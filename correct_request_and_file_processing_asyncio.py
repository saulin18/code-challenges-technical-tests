import asyncio
import os
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import aiofiles
import httpx
from PIL import Image

DOWNLOAD_LIMIT = 4
CPU_WORKERS = os.cpu_count()


IMAGE_URLS = [
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1532009324734-20a7a5813719?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1524429656589-6633a470097c?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1564135624576-c5c88640f235?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1522364723953-452d3431c267?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1516972810927-80185027ca84?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1550439062-609e1531270e?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1549692520-acc6669e2f0c?w=1920&h=1080&fit=crop",
]


ORIGINAL_DIR = Path("original_images")
PROCESSED_DIR = Path("processed_images")


async def download_single_image(
    client: httpx.AsyncClient,
    url: str,
    img_num: int,
    semaphore: asyncio.Semaphore,
) -> Path:
    async with semaphore:
        print(f"Downloading {url}...")
        ts = int(time.time())
        url = f"{url}?ts={ts}"  # Add timestamp to avoid caching issues

        response = await client.get(url, timeout=10, follow_redirects=True)
        response.raise_for_status()

        filename = f"image_{img_num}.jpg"
        download_path = ORIGINAL_DIR / filename

        async with aiofiles.open(download_path, "wb") as f:
            async for chunk in response.aiter_bytes(chunk_size=8192):
                await f.write(chunk)

        print(f"Downloaded and saved to: {download_path}")

        return download_path


async def download_images(urls: list) -> list[Path]:
    dl_semaphore = asyncio.Semaphore(DOWNLOAD_LIMIT)
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(
                    download_single_image(client, url, img_num, dl_semaphore)
                )
                for img_num, url in enumerate(urls, start=1)
            ]

        img_paths = [task.result() for task in tasks]

    return img_paths


def process_single_image(orig_path: Path) -> Path:
    save_path = PROCESSED_DIR / orig_path.name

    with Image.open(orig_path) as img:
        data = list(img.getdata())
        width, height = img.size
        new_data = []

        for i in range(len(data)):
            current_r, current_g, current_b = data[i]

            total_diff = 0
            neighbor_count = 0

            for dx, dy in [(1, 0), (0, 1)]:
                x = (i % width) + dx
                y = (i // width) + dy

                if 0 <= x < width and 0 <= y < height:
                    neighbor_r, neighbor_g, neighbor_b = data[y * width + x]
                    diff = (
                        abs(current_r - neighbor_r)
                        + abs(current_g - neighbor_g)
                        + abs(current_b - neighbor_b)
                    )
                    total_diff += diff
                    neighbor_count += 1

            if neighbor_count > 0:
                edge_strength = total_diff // neighbor_count
                if edge_strength > 30:
                    new_data.append((255, 255, 255))
                else:
                    new_data.append((0, 0, 0))
            else:
                new_data.append((0, 0, 0))

        edge_img = Image.new("RGB", (width, height))
        edge_img.putdata(new_data)
        edge_img.save(save_path)

    print(f"Processed {orig_path} and saved to {save_path}")
    return save_path


async def process_images(orig_paths: list[Path]) -> list[Path]:
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor(max_workers=CPU_WORKERS) as executor:
        tasks = [
            loop.run_in_executor(executor, process_single_image, orig_path)
            for orig_path in orig_paths
        ]

        processed_paths = await asyncio.gather(*tasks)

    return processed_paths


async def main():
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    start_time = time.perf_counter()

    img_paths = await download_images(IMAGE_URLS)

    proc_start_time = time.perf_counter()

    processed_paths = await process_images(img_paths)

    finished_time = time.perf_counter()

    dl_total_time = proc_start_time - start_time
    proc_total_time = finished_time - proc_start_time
    total_time = finished_time - start_time

    print(
        f"\nDownloaded {len(img_paths)} images in: {dl_total_time:.2f} seconds. {(dl_total_time / total_time) * 100:.2f}% of total time",
    )
    print(
        f"Processed {len(processed_paths)} images in: {proc_total_time:.2f} seconds. {(proc_total_time / total_time) * 100:.2f}% of total time",
    )
    print(
        f"\nTotal execution time: {total_time:.2f} seconds. {(total_time / total_time) * 100:.2f}% of total time",
    )


if __name__ == "__main__":
    asyncio.run(main())

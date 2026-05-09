import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const stream = new ReadableStream({
    start(controller) {
      const encoder = new TextEncoder();

      controller.enqueue(
        encoder.encode(
          `data: ${JSON.stringify({ message: "Connected!" })}\n\n`,
        ),
      );

      const interval = setInterval(() => {
        const data = {
          time: new Date().toISOString(),
          timestamp: Date.now(),
        };

        controller.enqueue(encoder.encode(`data: ${JSON.stringify(data)}\n\n`));
      }, 1000);

      request.signal.addEventListener("abort", () => {
        clearInterval(interval);
      });
    },
    pull() {
        
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "X-Accel-Buffering": "no",
    },
  });
}

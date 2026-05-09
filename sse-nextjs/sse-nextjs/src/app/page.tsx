import TimeDisplay from "@/components/TimeDisplay";
import Image from "next/image";
import Link from "next/link";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-centerfont-san">
      <main className="flex flex-1 w-full max-w-3xl flex-col items-center justify-between py-32 px-16 sm:items-start">
        <TimeDisplay />

        <Link  href="/notifications">
          Go to notifications
        </Link>
      </main>
    </div>
  );
}

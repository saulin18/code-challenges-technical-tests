import { NextRequest } from "next/server";
import { notificationService } from "@/lib/NotificationService";

export async function GET(request: NextRequest) {

    const encoder = new TextEncoder();
    const stream = new ReadableStream({

        start(controller) {

            // Send all notifications
            const notifications = notificationService.getNotifications();
            notifications.forEach((notification) => {
                controller.enqueue(encoder.encode
                    (`data: ${JSON.stringify({ type: 'notification', notification })}\n\n`));
            });


            //Subscribe to new notifications
            const subscription = notificationService.subscribe((notification) => {
                controller.enqueue(encoder.encode
                    (`data: ${JSON.stringify({ type: 'notification', notification, "receivedAt": new Date() })}\n\n`));
            });


            //Send a heartbeat every 10 seconds to keep the connection alive
            const heartbeat = setInterval(() => {
                controller.enqueue(encoder.encode(`data: ${JSON.stringify({ type: 'heartbeat' })}\n\n`));
            }, 10000);


            request.signal.addEventListener("abort", () => {
                subscription();
                clearInterval(heartbeat);
                controller.close();
            });

        }
    });

    return new Response(stream, {
        headers: {
            "Content-Type": "text/event-stream",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            'X-Accel-Buffering': 'no',
        },
    });


}
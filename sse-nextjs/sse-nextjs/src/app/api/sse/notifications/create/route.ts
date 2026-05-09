import { NextRequest, NextResponse } from "next/server";
import { notificationService } from "@/lib/NotificationService";

export async function POST(request: NextRequest) {

    try {



        const { title, message, type } = await request.json();

        if (!title || !message || !type) {
            return NextResponse.json({ error: "Missing required fields" }, { status: 400 });
        }

        notificationService.emit({ title, message, type });

        return NextResponse.json({ message: "Notification created successfully" }, { status: 201 });
    }
    catch (error) {
        return NextResponse.json({ error: `Invalid request, ${error}` }, { status: 500 });
    }

}
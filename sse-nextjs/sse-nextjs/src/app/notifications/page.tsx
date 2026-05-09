"use client";

import NotificationCenter from "@/components/NotificationCenter";
import { useActionState } from "react";

 /**
   * Server action to send notifications via SSE
   * @param type Notification Type
   */
 const sendNotification = async (
  prevState: { success: boolean | null } = { success: null },
  formData: FormData,
): Promise<{ success: boolean | null }> => {

 

  const type = formData.get("type") as string;

  if (!type) {
    console.error("Notification type is required");
    return { success: false };
  }

  try {
    await fetch("/api/sse/notifications/create", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        type,
        title: `New ${type} notification`,
        message: `This is a ${type} notification`,
      }),
    });
    return { success: true };
  } catch (error) {
    console.error("Error sending notification:", error);
    return { success: false };
  }
};


const NotificationsDashboard = () => {
 

  const [state, submitAction, isPending] = useActionState(sendNotification, {
    success: false,
  });

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header with Notification Center */}
      <header className="border-b border-gray-200 bg-white">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4">
          <h1 className="text-2xl font-bold">Notification Demo</h1>
          <NotificationCenter />
        </div>
      </header>

      {/* Main Content */}
      <main className="mx-auto max-w-7xl p-8">
        <div className="rounded-lg bg-white p-6 shadow-sm">
          <h2 className="mb-4 text-xl font-bold">Send Test Notifications</h2>
          <p className="mb-6 text-gray-600">
            Click the buttons below to trigger different types of notifications
          </p>

          <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            <form action={submitAction}>
              <input type="hidden" name="type" value="info" />
              <button
                type="submit"
                disabled={isPending}
                className="rounded-lg bg-blue-500 px-6 py-3 font-semibold text-white transition-colors hover:bg-blue-600 disabled:opacity-50"
              >
                Info Notification
              </button>
            </form>

            <form action={submitAction}>
              <input type="hidden" name="type" value="success" />
              <button
                type="submit"
                disabled={isPending}
                className="rounded-lg bg-green-500 px-6 py-3 font-semibold text-white transition-colors hover:bg-green-600 disabled:opacity-50"
              >
                Success Notification
              </button>
            </form>

            <form action={submitAction}>
              <input type="hidden" name="type" value="warning" />
              <button
                type="submit"
                disabled={isPending}
                className="rounded-lg bg-yellow-500 px-6 py-3 font-semibold text-white transition-colors hover:bg-yellow-600 disabled:opacity-50"
              >
                Warning Notification
              </button>
            </form>

            <form action={submitAction}>
              <input type="hidden" name="type" value="error" />

              <button
                type="submit"
                disabled={isPending}
                className="rounded-lg bg-red-500 px-6 py-3 font-semibold text-white transition-colors hover:bg-red-600 disabled:opacity-50"
              >
                Error Notification
              </button>
            </form>
          </div>
        </div>
      </main>
    </div>
  );
};

export default NotificationsDashboard;

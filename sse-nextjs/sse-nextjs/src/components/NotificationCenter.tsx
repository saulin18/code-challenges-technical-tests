"use client";
import { useState, useEffect } from "react";
import { Notification } from "@/lib/NotificationService";
import React from "react";

export const NotificationCenter = () => {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [isOpen, setIsOpen] = useState(false);

  const unreadCount = notifications.filter((n) => !n.read).length;

  useEffect(() => {
    const eventSource = new EventSource("/api/sse/notifications");

    eventSource.onmessage = (event) => {
      const notification = JSON.parse(event.data);
      setNotifications((prev) => [...prev, notification]);
    };

    eventSource.onerror = (event) => {
      console.error("EventSource failed:", event);
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, []);

  const getIcon = (type: Notification["type"]) => {
    switch (type) {
      case "error":
        return "❌";
      case "warning":
        return "⚠️";
        break;
      case "success":
        return "✅";
      case "info":
        return "ℹ️";
      default:
        break;
    }
  };

  const getColor = (type: Notification["type"]) => {
    switch (type) {
      case "success":
        return "border-green-500 bg-green-50";
      case "error":
        return "border-red-500 bg-red-50";
      case "warning":
        return "border-yellow-500 bg-yellow-50";
      default:
        return "border-blue-500 bg-blue-50";
    }
  };

  return (
    <div className="relative">
      {/* Notification Bell */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="relative rounded-full p-2 hover:bg-gray-100"
      >
        <svg
          className="h-6 w-6"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
          />
        </svg>
        {unreadCount > 0 && (
          <span className="absolute right-0 top-0 flex h-5 w-5 items-center justify-center rounded-full bg-red-500 text-xs text-white">
            {unreadCount}
          </span>
        )}
      </button>

      {/* Notification Panel */}
      {isOpen && (
        <div className="absolute right-0 top-12 z-50 w-80 rounded-lg border border-gray-200 bg-white shadow-xl">
          <div className="border-b border-gray-200 p-4">
            <h3 className="font-bold">Notifications</h3>
          </div>
          <div className="max-h-96 overflow-y-auto">
            {notifications.length === 0 ? (
              <p className="p-4 text-center text-gray-500">No notifications</p>
            ) : (
              notifications.map((notification) => (
                <div
                  key={notification.id}
                  className={`border-l-4 p-4 ${getColor(notification.type)} ${
                    notification.read ? "opacity-60" : ""
                  }`}
                >
                  <div className="flex items-start gap-3">
                    <span className="text-2xl">
                      {getIcon(notification.type)}
                    </span>
                    <div className="flex-1">
                      <h4 className="font-semibold">{notification.title}</h4>
                      <p className="text-sm text-gray-600">
                        {notification.message}
                      </p>
                      <p className="mt-1 text-xs text-gray-400">
                        {new Date(notification.timestamp).toLocaleTimeString()}
                      </p>
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default NotificationCenter;

CREATE TYPE "roles" AS ENUM('admin', 'user');--> statement-breakpoint
CREATE TYPE "statuses" AS ENUM('active', 'inactive');--> statement-breakpoint
CREATE TABLE "task_statuses" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"name" text NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "tasks" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"title" text NOT NULL,
	"description" text NOT NULL,
	"starting_time" timestamp DEFAULT now(),
	"ending_time" timestamp,
	"user_id" uuid,
	"assigned_to" uuid,
	"status" uuid,
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp DEFAULT now() NOT NULL
);
--> statement-breakpoint
CREATE TABLE "users" (
	"id" uuid PRIMARY KEY DEFAULT gen_random_uuid() NOT NULL,
	"email" text NOT NULL,
	"hashed_password" text NOT NULL,
	"first_name" text NOT NULL,
	"last_name" text NOT NULL,
	"profile_picture" text,
	"role" "roles" DEFAULT 'user' NOT NULL,
	"status" "statuses" DEFAULT 'active' NOT NULL,
	"created_at" timestamp DEFAULT now() NOT NULL,
	"updated_at" timestamp DEFAULT now() NOT NULL,
	CONSTRAINT "users_email_unique" UNIQUE("email")
);
--> statement-breakpoint
ALTER TABLE "tasks" ADD CONSTRAINT "tasks_user_id_users_id_fk" FOREIGN KEY ("user_id") REFERENCES "public"."users"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "tasks" ADD CONSTRAINT "tasks_assigned_to_users_id_fk" FOREIGN KEY ("assigned_to") REFERENCES "public"."users"("id") ON DELETE no action ON UPDATE no action;--> statement-breakpoint
ALTER TABLE "tasks" ADD CONSTRAINT "tasks_status_task_statuses_id_fk" FOREIGN KEY ("status") REFERENCES "public"."task_statuses"("id") ON DELETE no action ON UPDATE no action;
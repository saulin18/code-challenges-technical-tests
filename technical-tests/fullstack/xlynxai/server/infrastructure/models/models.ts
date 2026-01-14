import { pgEnum, pgTable, text, timestamp, uuid } from "drizzle-orm/pg-core";
import { userRoles, userStatus } from "../../domain/constants";


const roles = pgEnum("roles", Object.values(userRoles) as [string, ...string[]]);
const statuses = pgEnum("statuses", Object.values(userStatus) as [string, ...string[]]);

/*

When this file comes to more models, we can move this to a separate file for each model and have a index 
for building the schema who is used in database.ts
 */


export const usersTable = pgTable("users", {
    id: uuid("id").primaryKey().defaultRandom(),
    email: text("email").notNull().unique(),
    hashedPassword: text("hashed_password").notNull(),
    firstName: text("first_name").notNull(),
    lastName: text("last_name").notNull(),
    profilePicture: text("profile_picture"),
    role: roles("role").notNull().default(userRoles.USER),
    status: statuses("status").notNull().default(userStatus.ACTIVE),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export const taskStatusesTable = pgTable("task_statuses", {
    id: uuid("id").primaryKey().defaultRandom(),
    name: text("name").notNull(),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
});

export const tasksTable = pgTable("tasks", {
    id: uuid("id").primaryKey().defaultRandom(),
    title: text("title").notNull(),
    description: text("description").notNull(),
    startingTime: timestamp("starting_time").defaultNow(),
    endingTime: timestamp("ending_time"),
    userId: uuid("user_id").references(() => usersTable.id),
    assignedTo: uuid("assigned_to").references(() => usersTable.id),
    statusId: uuid("status").references(() => taskStatusesTable.id),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
});


export const refreshTokensTable = pgTable("refresh_tokens", {
    id: uuid("id").primaryKey().defaultRandom(),
    token: text("token").notNull(),
    userId: uuid("user_id").references(() => usersTable.id),
    expiresAt: timestamp("expires_at").notNull(),
    createdAt: timestamp("created_at").notNull().defaultNow(),
    updatedAt: timestamp("updated_at").notNull().defaultNow(),
});
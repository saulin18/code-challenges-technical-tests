import { ITaskRepository } from "../../domain/interfaces/task-repository";
import { tasksTable } from "../models/models";
import { eq } from "drizzle-orm";
import { AppDatabase } from "../database";
import { Task, TaskStatus } from "../../domain/entities/tasks";
import { Result } from "../../shared/result";
import { DATABASE_CODE_ERROR } from "./user-repository";
import { PgTransaction } from "drizzle-orm/pg-core";

export const taskRepository = (database: AppDatabase, transaction?: PgTransaction<any, any, any>): ITaskRepository => {
        const db = transaction ?? database;

    const toDomainTask = (task: typeof tasksTable.$inferSelect): Task => {
        return {
            id: task.id,
            title: task.title,
            description: task.description,
            statusId: task.statusId ?? "",
            assignedTo: task.assignedTo ?? "",
            startingTime: task.startingTime ?? new Date(),
            endingTime: task.endingTime ?? new Date(),
            userId: task.userId ?? "",
            createdAt: task.createdAt,
            updatedAt: task.updatedAt,
        }
    }


    return {

        create: async (task) => {
            try {
                console.log("🔵 [TASK-REPO] Inserting task:", JSON.stringify(task, null, 2));
                // Convertir valores vacíos a null para campos opcionales
                const taskToInsert = {
                    ...task,
                    statusId: task.statusId && task.statusId.trim() !== "" ? task.statusId : null,
                    assignedTo: task.assignedTo && task.assignedTo.trim() !== "" ? task.assignedTo : null,
                    endingTime: task.endingTime || null,
                };
                console.log("🔵 [TASK-REPO] Task to insert (with nulls):", JSON.stringify(taskToInsert, null, 2));
                const result = await db.insert(tasksTable).values(taskToInsert).returning();
                console.log("✅ [TASK-REPO] Task inserted successfully");
                return result.length > 0 ? Result.ok(toDomainTask(result[0])) : Result.err("Failed to create task", DATABASE_CODE_ERROR);
            } catch (error) {
                console.log("🔴 [TASK-REPO] Database error:", error);
                return Result.err("Failed to create task: " + (error instanceof Error ? error.message : String(error)), DATABASE_CODE_ERROR);
            }
        },

        list: async (userId, limit, offset) => {
            const result = await db.select().from(tasksTable).where(eq(tasksTable.userId, userId)).limit(limit).offset(offset);
            return Result.ok(result.map(toDomainTask));
        },

        getById: async (id) => {
            const result = await db.select().from(tasksTable).where(eq(tasksTable.id, id)).limit(1);
            return result.length > 0 ? Result.ok(toDomainTask(result[0])) : Result.err("Task not found", DATABASE_CODE_ERROR);
        },

        update: async (task) => {
            const result = await db.update(tasksTable).set(task).where(eq(tasksTable.id, task.id)).returning();
            return result.length > 0 ? Result.ok(toDomainTask(result[0])) : Result.err("Failed to update task", DATABASE_CODE_ERROR);
        },

        delete: async (id) => {
            const result = await db.delete(tasksTable).where(eq(tasksTable.id, id)).returning();
            return result.length > 0 ? Result.ok(undefined) : Result.err("Failed to delete task", DATABASE_CODE_ERROR);
        },

    }


}
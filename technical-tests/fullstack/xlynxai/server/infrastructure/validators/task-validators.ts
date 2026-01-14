import { createInsertSchema, createUpdateSchema } from "drizzle-zod";
import { tasksTable } from "../models/models";
import { uuid, z } from "zod";

export const taskInsertSchema = createInsertSchema(tasksTable, {
    title: (schema) => schema.min(1, "Title is required").max(200, "Title must be less than 200 characters"),
    description: (schema) => schema.min(1, "Description is required").max(1000, "Description must be less than 1000 characters"),
    userId: (schema) => schema.refine(() => uuid(schema as any)).optional(),
    assignedTo: (schema) => schema.refine(() => uuid(schema as any)).optional(),
    statusId: (schema) => schema.refine(() => uuid(schema as any)).optional(),
    startingTime: (schema) => schema.optional(),
    endingTime: (schema) => schema.optional(),
});


export const taskUpdateSchema = createUpdateSchema(tasksTable, {
    title: (schema) => schema.min(1).max(200).optional(),
    description: (schema) => schema.min(1).max(1000).optional(),
    assignedTo: (schema) => schema.refine(() => uuid(schema as any)).optional(),
    statusId: (schema) => schema.refine(() => uuid(schema as any)).optional(),
    startingTime: (schema) => schema.optional(),
    endingTime: (schema) => schema.optional(),
});

export type TaskInsertInput = z.infer<typeof taskInsertSchema>;
export type TaskUpdateInput = z.infer<typeof taskUpdateSchema>;


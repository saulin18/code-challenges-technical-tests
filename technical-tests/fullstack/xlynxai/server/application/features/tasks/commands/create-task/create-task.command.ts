import { Result } from "../../../../../shared/result";
import { Task } from "../../../../../domain/entities/tasks";
import { z } from "zod";

export const createTaskCommandSchema = z.object({
    title: z.string().min(1).max(200),
    description: z.string().min(1).max(1000),
    userId: z.uuid(),
    assignedTo: z.uuid().optional(),
    statusId: z.uuid().optional(),
    startingTime: z.coerce.date(),
    endingTime: z.coerce.date().optional(),
});

export type CreateTaskCommand = z.infer<typeof createTaskCommandSchema>;
export type CreateTaskResult = Result<Task>;


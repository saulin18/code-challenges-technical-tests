import { Result } from "../../../../../shared/result";
import { Task } from "../../../../../domain/entities/tasks";
import { z } from "zod";

export const updateTaskCommandSchema = z.object({
    id: z.string().uuid(),
    title: z.string().min(1).max(200).optional(),
    description: z.string().min(1).max(1000).optional(),
    assignedTo: z.string().uuid().optional(),
    statusId: z.string().uuid().optional(),
    endingTime: z.coerce.date().optional(),
});

export type UpdateTaskCommand = z.infer<typeof updateTaskCommandSchema>;
export type UpdateTaskResult = Result<Task>;


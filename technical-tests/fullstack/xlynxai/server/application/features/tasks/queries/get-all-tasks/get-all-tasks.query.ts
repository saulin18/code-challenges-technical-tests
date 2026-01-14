import { Result } from "../../../../../shared/result";
import { Task } from "../../../../../domain/entities/tasks";
import { z } from "zod";

export const getAllTasksQuerySchema = z.object({
    userId: z.string().uuid().optional(),
    limit: z.coerce.number().min(1).max(100).default(10),
    offset: z.coerce.number().min(0).default(0),
});

export type GetAllTasksQuery = z.infer<typeof getAllTasksQuerySchema>;
export type GetAllTasksResult = Result<Task[]>;


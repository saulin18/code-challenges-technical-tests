import { Result } from "../../../../../shared/result";
import { Task } from "../../../../../domain/entities/tasks";
import { z } from "zod";

export const getTaskQuerySchema = z.object({
    id: z.string().uuid(),
});

export type GetTaskQuery = z.infer<typeof getTaskQuerySchema>;
export type GetTaskResult = Result<Task>;


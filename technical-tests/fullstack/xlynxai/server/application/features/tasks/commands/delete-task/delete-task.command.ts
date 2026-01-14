import { Result } from "../../../../../shared/result";
import { z } from "zod";

export const deleteTaskCommandSchema = z.object({
    id: z.string().uuid(),
});

export type DeleteTaskCommand = z.infer<typeof deleteTaskCommandSchema>;
export type DeleteTaskResult = Result<void>;


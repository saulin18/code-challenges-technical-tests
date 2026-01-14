import { Result } from "../../../../../shared/result";
import { z } from "zod";

export const deleteUserCommandSchema = z.object({
    id: z.uuid()
});

export type DeleteUserCommand = z.infer<typeof deleteUserCommandSchema>;
export type DeleteUserResult = Result<void>;


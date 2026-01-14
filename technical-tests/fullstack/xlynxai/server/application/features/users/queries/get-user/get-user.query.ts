import { Result } from "../../../../../shared/result";
import { User } from "../../../../../domain/entities/user";
import { z } from "zod";

export const getUserQuerySchema = z.object({
    id: z.string().uuid(),
});

export type GetUserQuery = z.infer<typeof getUserQuerySchema>;
export type GetUserResult = Result<User>;


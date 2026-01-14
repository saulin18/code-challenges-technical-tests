import { Result } from "../../../../../shared/result";
import { z } from "zod";
import { User } from "../../../../../domain/entities/user";

export const logInUserCommandSchema = z.object({
    email: z.email(),
    password: z.string().min(1),
});

export type LogInUserCommand = z.infer<typeof logInUserCommandSchema>;
export type LogInUserResult = Result<{ accessToken: string; refreshToken: string }>;


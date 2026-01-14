import { Result } from "../../../../../shared/result";
import { User } from "../../../../../domain/entities/user";
import { z } from "zod";

export const registerUserCommandSchema = z.object({
    email: z.string().email(),
    password: z.string().min(8),
    firstName: z.string().min(1).max(100),
    lastName: z.string().min(1).max(100),
});

export type RegisterUserCommand = z.infer<typeof registerUserCommandSchema>;
export type RegisterUserResult = Result<User>;


import { Result } from "../../../../../shared/result";
import { User } from "../../../../../domain/entities/user";
import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { z } from "zod";

export const getAllUsersQuerySchema = z.object({
    limit: z.number().min(1).max(100).default(10),
    offset: z.number().min(0).default(0),
});

export type GetAllUsersQuery = z.infer<typeof getAllUsersQuerySchema>;

export type GetAllUsersResult = Result<User[]>;
import { Result } from "../../../../../shared/result";
import { User } from "../../../../../domain/entities/user";
import { z } from "zod";

export const updateProfileCommandSchema = z.object({
    id: z.uuid(),
    firstName: z.string().min(1).max(100).optional(),
    lastName: z.string().min(1).max(100).optional(),
    profilePicture: z.string().url().nullable().optional(),
});

export type UpdateProfileCommand = z.infer<typeof updateProfileCommandSchema>;
export type UpdateProfileResult = Result<User>;


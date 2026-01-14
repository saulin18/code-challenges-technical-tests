import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { Result } from "../../../../../shared/result";
import { GetAllUsersQuery, GetAllUsersResult } from "./get-all-users-query";
import { z } from "zod";


export async function getAllUsers(
    userRepository: UserRepository,
    query: GetAllUsersQuery
): Promise<GetAllUsersResult> {
    const result = await userRepository.getAll(query.limit, query.offset);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}
import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { Result } from "../../../../../shared/result";
import { GetUserQuery, GetUserResult } from "./get-user.query";

export async function getUser(
    userRepository: UserRepository,
    query: GetUserQuery
): Promise<GetUserResult> {
    const result = await userRepository.getById(query.id);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}


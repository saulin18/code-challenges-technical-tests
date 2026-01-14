import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { Result } from "../../../../../shared/result";
import { DeleteUserCommand, DeleteUserResult } from "./delete-user.command";

export async function deleteUser(
    userRepository: UserRepository,
    command: DeleteUserCommand
): Promise<DeleteUserResult> {
    const existingUser = await userRepository.getById(command.id);
    if (!existingUser.ok) {
        return Result.err("User not found", "NOT_FOUND");
    }

    const result = await userRepository.delete(command.id);

    if (!result.ok) {
        return result;
    }

    return Result.ok(undefined);
}


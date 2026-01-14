import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { User } from "../../../../../domain/entities/user";
import { Result } from "../../../../../shared/result";
import { UpdateProfileCommand, UpdateProfileResult } from "./update-profile.command";

export async function updateProfile(
    userRepository: UserRepository,
    command: UpdateProfileCommand
): Promise<UpdateProfileResult> {
    
    const existingUserResult = await userRepository.getById(command.id);
    if (!existingUserResult.ok) {
        return Result.err("User not found", "NOT_FOUND");
    }

    
    const { id, ...updates } = command;
    const updateData: Required<Pick<User, "id"> & Partial<User>> = {
        id,
        ...User.updatePersonalInformation(updates),
        email: existingUserResult.data.email,
        hashedPassword: existingUserResult.data.hashedPassword,
        role: existingUserResult.data.role,
        status: existingUserResult.data.status,
        createdAt: existingUserResult.data.createdAt,
        firstName: existingUserResult.data.firstName,
        lastName: existingUserResult.data.lastName,
        profilePicture: existingUserResult.data.profilePicture,
        updatedAt: new Date(),
    };

    const result = await userRepository.updateProfile(updateData);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}


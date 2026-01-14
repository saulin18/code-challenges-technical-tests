import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { User } from "../../../../../domain/entities/user";
import { Result } from "../../../../../shared/result";
import { RegisterUserCommand, RegisterUserResult } from "./register-user.command";
import { AuthService } from "../../../../../application/interfaces/auth-service";



export async function registerUser(
    userRepository: UserRepository,
    authService: AuthService,
    command: RegisterUserCommand
): Promise<RegisterUserResult> {

    const existingUser = await userRepository.getByEmail(command.email);
    if (existingUser.ok) {
        return Result.err("User with this email already exists", "VALIDATION_ERROR");
    }

    const hashedPassword = await authService.hashPassword(command.password);

    
    const newUser = User.create({
        email: command.email,
        hashedPassword,
        firstName: command.firstName,
        lastName: command.lastName,
        profilePicture: null,
        role: "user",
        status: "active",
        });

    const userData: Omit<User, "id" | "createdAt" | "updatedAt"> = {
        email: newUser.email,
        hashedPassword: newUser.hashedPassword,
        firstName: newUser.firstName,
        lastName: newUser.lastName,
        profilePicture: newUser.profilePicture,
        role: newUser.role,
        status: newUser.status,
    };

    const result = await userRepository.create(userData);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}


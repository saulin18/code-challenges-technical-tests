import { UserRepository } from "../../../../../domain/interfaces/user-repository";
import { Result } from "../../../../../shared/result";
import { LogInUserCommand, LogInUserResult } from "./log-in-user.command";
import { AuthService } from "../../../../../application/interfaces/auth-service";

export async function logInUser(
  userRepository: UserRepository,
  authService: AuthService,
  command: LogInUserCommand
): Promise<LogInUserResult> {
  const user = await userRepository.getByEmail(command.email);
  if (!user.ok) {
    return Result.err("Invalid email or password", "UNAUTHORIZED");
  }

  const isPasswordValid = await authService.comparePassword(
    command.password,
    user.data.hashedPassword
  );
  if (!isPasswordValid) {
    return Result.err("Invalid email or password", "UNAUTHORIZED");
  }

  const accessToken = authService.generateAccessToken({
    id: user.data.id,
    email: user.data.email,
    role: user.data.role,
    status: user.data.status,
  });
  const refreshToken = authService.generateRefreshToken({
    id: user.data.id,
    email: user.data.email,
    role: user.data.role,
    status: user.data.status,
  });

  const expiresAt = new Date();
  expiresAt.setDate(expiresAt.getDate() + 7);

  await authService.saveRefreshToken(refreshToken, user.data.id, expiresAt);

  return Result.ok({ accessToken, refreshToken });
}

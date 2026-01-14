import { useMutation } from "@tanstack/react-query";
import type { AuthService } from "../auth-service";
import { throwResultError } from "../../../common/result";
import { useAuthContext } from "../auth-context";


export const useAuth = (authService: AuthService) => {
  const { setAuth } = useAuthContext();

  const register = useMutation({
    meta: {
      successMessage: "User registered successfully",
      errorMessage: "Failed to register user",
    },
    mutationFn: async ({
      email,
      password,
      firstName,
      lastName,
    }: {
      email: string;
      password: string;
      firstName: string;
      lastName: string;
    }) => {
      const result = await authService.register(
        email,
        password,
        firstName,
        lastName
      );
      return throwResultError(result);
    },
    onSuccess: (data) => {
      setAuth(data.accessToken, data.refreshToken);
    },
  });

  const login = useMutation({
    meta: {
      successMessage: "User logged in successfully",
      errorMessage: "Failed to login user",
    },
    mutationFn: async ({ email, password }: { email: string; password: string }) => {
      const result = await authService.login(email, password);
      return throwResultError(result);
    },
    onSuccess: (data) => {
      setAuth(data.accessToken, data.refreshToken);
    },
  });

  return {
    register,
    login,
  };
};

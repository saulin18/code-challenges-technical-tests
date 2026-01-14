import { Result } from "../../common/result";
import { getApiUrl } from "../../common/api-config";
import type { User } from "./types";

export interface AuthService {
  login: (
    email: string,
    password: string
  ) => Promise<Result<{ accessToken: string; refreshToken: string; user: User }>>;
  register: (
    email: string,
    password: string,
    firstName: string,
    lastName: string
  ) => Promise<Result<{ accessToken: string; refreshToken: string }>>;
}


interface ProblemDetails {
  status: number;
  title: string;
  detail?: string;
  type?: string;
  [key: string]: any;
}

export const authService = (): AuthService => {
  return {
    login: async (email: string, password: string) => {
      const response = await fetch(getApiUrl(`/users/login`), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      const data = await response.json();

      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to login", 
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }

      return Result.ok({
        accessToken: data.accessToken,
        refreshToken: data.refreshToken,
        user: data.user,
      });
    },
    register: async (
      email: string,
      password: string,
      firstName: string,
      lastName: string
    ) => {
      const response = await fetch(getApiUrl(`/users/register`), {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password, firstName, lastName }),
      });

      const data = await response.json();

      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to register", 
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }

      return Result.ok({
        accessToken: data.accessToken,
        refreshToken: data.refreshToken,
      });
    },
  };
};

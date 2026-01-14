import { User } from "../entities/user";
import { Result } from "../../shared/result";

export interface UserRepository {
  create: (
    user: Omit<User, "id" | "createdAt" | "updatedAt">
  ) => Promise<Result<User>>;

  getByEmail: (email: User["email"]) => Promise<Result<User>>;
  getAll: (limit: number, offset: number) => Promise<Result<User[]>>;
  updateProfile: (
    user: Required<Pick<User, "id"> & Partial<User>>
  ) => Promise<Result<User>>;
  delete: (id: string) => Promise<Result<void>>;
  getById: (id: string) => Promise<Result<User>>;
}

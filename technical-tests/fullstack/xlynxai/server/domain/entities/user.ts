import { userRoles, userStatus } from "../constants";

  export type User = {
  id: string;
  email: string;
  hashedPassword: string;
  firstName: string;
  lastName: string;
  profilePicture: string | null;
  role: typeof userRoles[keyof typeof userRoles];
  status: typeof userStatus[keyof typeof userStatus];
  createdAt: Date;
  updatedAt: Date;
};

export const User = {
  create: ({
    email,
    hashedPassword,
    firstName,
    lastName,
    profilePicture,
    role,
    status,
  }: Omit<User, "id" | "createdAt" | "updatedAt">): User => {
    return {
      id: crypto.randomUUID(),
      email,
      hashedPassword,
      firstName,
      lastName,
      profilePicture: profilePicture ?? null,
      role,
      status,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
  },

  updatePersonalInformation: (
    updates: Partial<Pick<User, "firstName" | "lastName" | "profilePicture">>
  ) => {
    return {
      ...updates,
      updatedAt: new Date(),
    };
  },

  getPermissions: (user: User): string[] => {
    const perms: string[] = [];

    if (user.role !== "admin") {
      perms.push(`tasks::read::owner:${user.id}`);
      perms.push(`tasks::write::owner:${user.id}`);
      perms.push(`users::read::owner:${user.id}`);
      return perms;
    }

    perms.push("tasks::all::all");
    perms.push("users::all::all");
    return perms;
  },
};

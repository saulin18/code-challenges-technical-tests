import { UserRepository } from "../../domain/interfaces/user-repository";
import { usersTable } from "../models/models";
import { eq } from "drizzle-orm";
import { AppDatabase, db } from "../database";
import { User } from "../../domain/entities/user";
import { Result } from "../../shared/result";
import { userRoles, userStatus } from "../../domain/constants";
import { PgTransaction } from "drizzle-orm/pg-core";

export const DATABASE_CODE_ERROR = "DATABASE_ERROR"

export const userRepository = (database: AppDatabase, transaction?: PgTransaction<any, any, any>): UserRepository => {
    const db = transaction ?? database;
    const toDomainUser = (user: typeof usersTable.$inferSelect): User => {

        const roleMap: Record<string, User["role"]> = {
            [userRoles.ADMIN]: "admin",
            [userRoles.USER]: "user",
        };
        const statusMap: Record<string, User["status"]> = {
            [userStatus.ACTIVE]: "active",
            [userStatus.INACTIVE]: "inactive",
        };
        
        return {
            id: user.id,
            email: user.email,
            hashedPassword: user.hashedPassword,
            firstName: user.firstName,
            lastName: user.lastName,
            profilePicture: user.profilePicture,
            role: roleMap[user.role] || (user.role as User["role"]),
            status: statusMap[user.status] || (user.status as User["status"]),
            createdAt: user.createdAt,
            updatedAt: user.updatedAt,
        }
    }
    return {
        create: async (user) => {
            const userExisting = await db.select().from(usersTable).where(eq(usersTable.email, user.email));
            if (userExisting.length > 0) {
                return Result.err("User already exists", DATABASE_CODE_ERROR);
            }

            const result = await db.insert(usersTable).values(user).returning();
            return result.length > 0 ? Result.ok(toDomainUser(result[0])) : Result.err("Failed to create user", DATABASE_CODE_ERROR);
        },

        getAll: async (limit, offset) => {
            const result = await db.select().from(usersTable).limit(limit).offset(offset);
            return result.length > 0 ? Result.ok(result.map(toDomainUser)) : Result.err("Failed to get users", DATABASE_CODE_ERROR);
        },

        getByEmail: async (email) => {
            const result = await db.select().from(usersTable).where(eq(usersTable.email, email)).limit(1)
            return result[0] ? Result.ok(toDomainUser(result[0])) : Result.err("Failure to get user", DATABASE_CODE_ERROR)
        },

        updateProfile: async (user) => {

            const result = await db.update(usersTable).set(user).where(eq(usersTable.id, user.id)).returning();
            return result.length > 0 ? Result.ok(toDomainUser(result[0])) : Result.err("Failed to update user", DATABASE_CODE_ERROR);
        },

        delete: async (id) => {
            const result = await db.update(usersTable).set({ status: userStatus.INACTIVE }).where(eq(usersTable.id, id)).returning();
            return result.length > 0 ? Result.ok(undefined) : Result.err("Failed to delete user", DATABASE_CODE_ERROR);
        },

        getById: async (id) => {
            const result = await db.select().from(usersTable).where(eq(usersTable.id, id)).limit(1);
            return result.length > 0 ? Result.ok(toDomainUser(result[0])) : Result.err("User not found", DATABASE_CODE_ERROR);
        },

    }
}
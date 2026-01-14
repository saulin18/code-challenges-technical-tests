import jwt from "jsonwebtoken";
import { AuthService } from "../../application/interfaces/auth-service";
import { User } from "../../domain/entities/user";
import bcrypt from "bcryptjs";
import { AppDatabase } from "../database";
import { refreshTokensTable } from "../models/models";
import { eq, and, gt } from "drizzle-orm";


export const authService = (database: AppDatabase): AuthService => {
    return {
        hashPassword: async (password: string) => {
            return await bcrypt.hash(password, 10);
        },
        comparePassword: async (password: string, hashed: string) => {
            return await bcrypt.compare(password, hashed);
        },
        generateAccessToken: (claims: Pick<User, "id" | "email" | "role" | "status">) => {
            return jwt.sign(claims, process.env.JWT_SECRET!, { expiresIn: '1h' });
        },
        verifyToken: (token: string) => {
            return jwt.verify(token, process.env.JWT_SECRET!);
        },
        decodeToken: (token: string) => {
            return jwt.decode(token);
        },
        generateRefreshToken: (claims: Pick<User, "id" | "email" | "role" | "status">) => {
            return jwt.sign(claims, process.env.JWT_SECRET!, { expiresIn: '7d' });
        },
        saveRefreshToken: async (token: string, userId: string, expiresAt: Date) => {
            await database.insert(refreshTokensTable).values({
                token,
                userId,
                expiresAt,
            });
        },
        verifyRefreshToken: async (token: string) => {
            try {

                const decoded = jwt.verify(token, process.env.JWT_SECRET!) as { id: string; exp: number };
  
                const result = await database
                    .select()
                    .from(refreshTokensTable)
                    .where(
                        and(
                            eq(refreshTokensTable.token, token),
                            eq(refreshTokensTable.userId, decoded.id),
                            gt(refreshTokensTable.expiresAt, new Date())
                        )
                    )
                    .limit(1);

                if (result.length === 0) {
                    return { valid: false };
                }

                return { valid: true, userId: decoded.id };
            } catch (error) {
                return { valid: false };
            }
        },
        revokeRefreshToken: async (token: string) => {
            await database.delete(refreshTokensTable).where(eq(refreshTokensTable.token, token));
        },
    }
}
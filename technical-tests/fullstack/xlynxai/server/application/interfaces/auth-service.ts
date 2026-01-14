import { User } from "../../domain/entities/user";

import jwt from "jsonwebtoken";

export interface AuthService {
    hashPassword: (password: string) => Promise<string>;
    comparePassword: (password: string, hashed: string) => Promise<boolean>;
    generateAccessToken: (claims: Pick<User, "id" | "email" | "role" | "status">) => string;
    verifyToken: (token: string) => string | jwt.JwtPayload;
    decodeToken: (token: string) => string | jwt.JwtPayload | null;
    generateRefreshToken: (claims: Pick<User, "id" | "email" | "role" | "status">) => string;
    saveRefreshToken: (token: string, userId: string, expiresAt: Date) => Promise<void>;
    verifyRefreshToken: (token: string) => Promise<{ valid: boolean; userId?: string }>;
    revokeRefreshToken: (token: string) => Promise<void>;
}

import { Request, Response, NextFunction } from "express";
import { AuthenticatedRequest } from "./permission-middleware";
import { authService } from "../../infrastructure/auth/auth-service";
import { userRepository } from "../../infrastructure/repositories/user-repository";
import { db } from "../../infrastructure/database";
import { ProblemDetails } from "../../shared/problem-details";

const auth = authService(db);

export async function authenticateToken(
    req: AuthenticatedRequest,
    res: Response,
    next: NextFunction
) {
    console.log("🔴 [AUTH] authenticateToken called for:", req.method, req.path, req.originalUrl);
    const authHeader = req.headers.authorization;
    const token = authHeader && authHeader.split(' ')[1];

    if (!token) {
        console.log("🔴 [AUTH] No token found, returning 401");
        const problem = ProblemDetails.create({
            status: 401,
            title: "Unauthorized",
            detail: "Authentication token is required",
            type: "UNAUTHORIZED",
            instance: req.originalUrl,
        });
        return res.status(401).json(problem);
    }

    try {
        const decoded = auth.verifyToken(token) as { id: string; email: string; role: string; status: string };
        
        const userRepo = userRepository(db);
        const userResult = await userRepo.getById(decoded.id);
        
        if (!userResult.ok) {
            const problem = ProblemDetails.create({
                status: 401,
                title: "Unauthorized",
                detail: "Invalid or expired token",
                type: "UNAUTHORIZED",
                instance: req.originalUrl,
            });
            return res.status(401).json(problem);
        }

        req.user = userResult.data;
        next();
    } catch (error) {
        const problem = ProblemDetails.create({
            status: 401,
            title: "Unauthorized",
            detail: "Invalid or expired token",
            type: "UNAUTHORIZED",
            instance: req.originalUrl,
        });
        return res.status(401).json(problem);
    }
}

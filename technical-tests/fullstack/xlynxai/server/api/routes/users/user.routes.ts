import { Router, Response, NextFunction } from "express";
import { db } from "../../../infrastructure/database";
import { userRepository } from "../../../infrastructure/repositories/user-repository";
import { authService } from "../../../infrastructure/auth/auth-service";
import { registerUser } from "../../../application/features/users/commands/register-user/register-user.handler";
import { updateProfile } from "../../../application/features/users/commands/update-profile/update-profile.handler";
import { deleteUser } from "../../../application/features/users/commands/delete-user/delete-user.handler";
import { getUser } from "../../../application/features/users/queries/get-user/get-user.handler";
import { getAllUsers } from "../../../application/features/users/queries/get-all-users/get-all-users-query-handler";
import { getAllUsersQuerySchema } from "../../../application/features/users/queries/get-all-users/get-all-users-query";
import { checkPermission, AuthenticatedRequest } from "../../middlewares/permission-middleware";
import { validate, ValidatedRequest } from "../../middlewares/validation-middleware";
import { registerUserCommandSchema } from "../../../application/features/users/commands/register-user/register-user.command";
import { logInUserCommandSchema } from "../../../application/features/users/commands/log-in-user/log-in-user.command";
import { updateProfileCommandSchema } from "../../../application/features/users/commands/update-profile/update-profile.command";
import { deleteUserCommandSchema } from "../../../application/features/users/commands/delete-user/delete-user.command";
import { getUserQuerySchema } from "../../../application/features/users/queries/get-user/get-user.query";
import { z } from "zod";
import { User } from "@/domain/entities/user";
import { resultToProblemDetails } from "../../../shared/result-to-problem";
import { logInUser } from "@/application/features/users/commands/log-in-user/log-in-user.handler";

export const userRoutes = Router();

const repository = userRepository(db);
const auth = authService(db);

userRoutes.post(
    "/register",
    validate({ body: registerUserCommandSchema }),
    async (req: ValidatedRequest, res: Response) => {
        const validatedData = req.validatedData!;

        const result = await registerUser(repository, auth, validatedData);

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        const claims: Pick<User, "id" | "email" | "role" | "status"> = {
            id: result.data.id,
            email: result.data.email,
            role: result.data.role,
            status: result.data.status,
        };

        const accessToken = auth.generateAccessToken(claims);
        const refreshToken = auth.generateRefreshToken(claims);
        
        const expiresAt = new Date();
        expiresAt.setDate(expiresAt.getDate() + 7);
        
        await auth.saveRefreshToken(refreshToken, result.data.id, expiresAt);

        return res.status(201).json({ 
            data: result.data, 
            accessToken, 
            refreshToken 
        });
    })

userRoutes.post(
    "/login",
    validate({ body: logInUserCommandSchema }),
    async (req: ValidatedRequest, res: Response) => {
        const validatedData = req.validatedData!;

        const result = await logInUser(repository, auth, validatedData);

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(200).json({ 
            accessToken: result.data.accessToken,
            refreshToken: result.data.refreshToken,
        });
    }
);

userRoutes.get(
    "/",
    checkPermission({ resource: "users", action: "read" }),
    validate({ query: getAllUsersQuerySchema }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedQuery = req.validatedQuery!;

        const result = await getAllUsers(repository, validatedQuery);

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(200).json({
            data: result.data,
            total: result.data.length,
        });
    }
);


userRoutes.get(
    "/:id",
    checkPermission({ resource: "users", action: "read" }),
    validate({ params: getUserQuerySchema }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedParams = req.validatedParams!;

        const result = await getUser(repository, { id: validatedParams.id });

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(200).json({ data: result.data });
    }
);

userRoutes.put(
    "/:id",
    checkPermission({ resource: "users", action: "update" }),
    validate({
        body: updateProfileCommandSchema.omit({ id: true }),
        params: z.object({ id: z.string().uuid() }),
    }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedParams = req.validatedParams!;
        const validatedData = req.validatedData!;

        const result = await updateProfile(repository, {
            id: validatedParams.id,
            ...validatedData,
        });

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(200).json({ data: result.data });
    }
);

userRoutes.delete(
    "/:id",
    checkPermission({ resource: "users", action: "delete" }),
    validate({ params: deleteUserCommandSchema }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedParams = req.validatedParams!;

        const result = await deleteUser(repository, { id: validatedParams.id });

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(204).send();
    }
);

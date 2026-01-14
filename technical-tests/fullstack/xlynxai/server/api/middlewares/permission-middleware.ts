import { Request, Response, NextFunction } from "express";
import { matchAny, generatePermissionQuery, PermissionContext } from "../../domain/permissions";
import { User } from "../../domain/entities/user";
import { ProblemDetails } from "../../shared/problem-details";

export interface AuthenticatedRequest extends Request {
    user?: User;
}

export function checkPermission(
    context: PermissionContext
) {
    return (req: AuthenticatedRequest, res: Response, next: NextFunction) => {
        if (!req.user) {
            const problem = ProblemDetails.create({
                status: 401,
                title: "Unauthorized",
                detail: "Authentication required",
                type: "UNAUTHORIZED",
                instance: req.originalUrl,
            });
            return res.status(401).json(problem);
        }

        const userPerms = User.getPermissions(req.user);
        const query = generatePermissionQuery(context);

        const hasPermission = matchAny(query, userPerms, context.owner ? true : false);

        if (!hasPermission) {
            const problem = ProblemDetails.create({
                status: 403,
                title: "Forbidden",
                detail: "You do not have permission to perform this action",
                type: "FORBIDDEN",
                instance: req.originalUrl,
            });
            return res.status(403).json(problem);
        }

        next();
    };
}
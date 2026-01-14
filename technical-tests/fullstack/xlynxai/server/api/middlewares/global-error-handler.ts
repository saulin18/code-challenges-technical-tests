import { Request, Response, NextFunction } from "express";
import { ProblemDetails } from "../../shared/problem-details";
import { ErrorResult, Result } from "../../shared/result";

const ERROR_CODE_TO_HTTP_STATUS: Record<string, number> = {
    "VALIDATION_ERROR": 400,
    "UNAUTHORIZED": 401,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "CONFLICT": 409,
    "INTERNAL_ERROR": 500,
};

export const globalErrorHandler = (
    err: Error | ErrorResult,
    req: Request,
    res: Response,
    next: NextFunction
) => {
    // First check if it's a regular Error
    if (err instanceof Error) {
        const problem = ProblemDetails.create({
            status: 500,
            title: "Internal Server Error",
            detail: err.message,
            instance: req.originalUrl,
            extensions: {
                ...(process.env.NODE_ENV === "development" && err.stack && {
                    stack: err.stack,
                }),
            },
        });
        
        return res.status(problem.status).json(problem);
    }

    // Then check if it's an ErrorResult
    if (Result.isError(err as Result<any>) && 'error' in err && err.error) {
        const errorResult = err as ErrorResult;
        const status = ERROR_CODE_TO_HTTP_STATUS[errorResult.error.code] || 500;
        
        const problem = ProblemDetails.create({
            status,
            title: errorResult.error.message,
            type: errorResult.error.code,
            instance: req.originalUrl,
            extensions: {
                code: errorResult.error.code,
                ...(process.env.NODE_ENV === "development" && errorResult.error.stack && {
                    stack: errorResult.error.stack,
                }),
            },
        });
        
        return res.status(problem.status).json(problem);
    }

    
    const problem = ProblemDetails.create({
        status: 500,
        title: "Internal Server Error",
        detail: "An unexpected error occurred",
        instance: req.originalUrl,
    });
    
    return res.status(problem.status).json(problem);
};
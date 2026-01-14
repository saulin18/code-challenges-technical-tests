import { ErrorResult, Result } from "./result";
import { ProblemDetails } from "./problem-details";

const ERROR_CODE_TO_HTTP_STATUS: Record<string, number> = {
    "VALIDATION_ERROR": 400,
    "UNAUTHORIZED": 401,
    "FORBIDDEN": 403,
    "NOT_FOUND": 404,
    "CONFLICT": 409,
    "INTERNAL_ERROR": 500,
};

export function resultToProblemDetails(
    result: ErrorResult,
    instance?: string
): ProblemDetails {
    const status = ERROR_CODE_TO_HTTP_STATUS[result.error.code] || 500;
    
    return ProblemDetails.create({
        status,
        title: result.error.message,
        type: result.error.code,
        instance,
        extensions: {
            code: result.error.code,
            ...(process.env.NODE_ENV === "development" && result.error.stack && {
                stack: result.error.stack,
            }),
        },
    });
}


import { Request, Response, NextFunction } from "express";
import { z } from "zod";
import { ProblemDetails } from "../../shared/problem-details";

export interface ValidatedRequest<T = any> extends Request {
    validatedData?: T;
    validatedQuery?: T;
    validatedParams?: T;
}

type ValidationOptions = {
    body?: z.ZodTypeAny;
    query?: z.ZodTypeAny;
    params?: z.ZodTypeAny;
};

function isZodSchema(value: ValidationOptions | z.ZodTypeAny): value is z.ZodTypeAny {
    return typeof (value as z.ZodTypeAny).safeParse === "function";
}

export function validate(options: ValidationOptions | z.ZodTypeAny) {
    return (req: ValidatedRequest, res: Response, next: NextFunction) => {
        try {
            
            if (isZodSchema(options)) {
                const result = options.safeParse(req.body);
                if (!result.success) {
                    const problem = ProblemDetails.create({
                        status: 400,
                        title: "Validation Error",
                        detail: result.error.issues.map(e => `${e.path.join('.')}: ${e.message}`).join(", "),
                        type: "VALIDATION_ERROR",
                    });
                    return res.status(400).json(problem);
                }
                req.validatedData = result.data;
                return next();
            }

           
            if (options.body) {
                console.log("🔵 [VALIDATION] Validating body:", JSON.stringify(req.body, null, 2));
                const result = options.body.safeParse(req.body);
                if (!result.success) {
                    console.log("🔴 [VALIDATION] Validation failed:", result.error.issues);
                    const problem = ProblemDetails.create({
                        status: 400,
                        title: "Validation Error",
                        detail: result.error.issues.map(e => `body.${e.path.join('.')}: ${e.message}`).join(", "),
                        type: "VALIDATION_ERROR",
                    });
                    return res.status(400).json(problem);
                }
                console.log("✅ [VALIDATION] Validation passed");
                req.validatedData = result.data;
            }

        
            if (options.query) {
                const result = options.query.safeParse(req.query);
                if (!result.success) {
                    const problem = ProblemDetails.create({
                        status: 400,
                        title: "Validation Error",
                        detail: result.error.issues.map(e => `query.${e.path.join('.')}: ${e.message}`).join(", "),
                        type: "VALIDATION_ERROR",
                    });
                    return res.status(400).json(problem);
                }
                req.validatedQuery = result.data;
            }

            if (options.params) {
                const result = options.params.safeParse(req.params);
                if (!result.success) {
                    const problem = ProblemDetails.create({
                        status: 400,
                        title: "Validation Error",
                        detail: result.error.issues.map(e => `params.${e.path.join('.')}: ${e.message}`).join(", "),
                        type: "VALIDATION_ERROR",
                    });
                    return res.status(400).json(problem);
                }
                req.validatedParams = result.data;
            }

            next();
        } catch (error) {
            const problem = ProblemDetails.create({
                status: 400,
                title: "Invalid request data",
                type: "VALIDATION_ERROR",
            });
            return res.status(400).json(problem);
        }
    };
}


import { Router, Response } from "express";
import { db } from "../../../infrastructure/database";
import { taskRepository } from "../../../infrastructure/repositories/task-repository";
import { createTask } from "../../../application/features/tasks/commands/create-task/create-task.handler";
import { updateTask } from "../../../application/features/tasks/commands/update-task/update-task.handler";
import { deleteTask } from "../../../application/features/tasks/commands/delete-task/delete-task.handler";
import { getAllTasks } from "../../../application/features/tasks/queries/get-all-tasks/get-all-tasks.handler";
import { getTask } from "../../../application/features/tasks/queries/get-task/get-task.handler";
import { checkPermission, AuthenticatedRequest } from "../../middlewares/permission-middleware";
import { validate, ValidatedRequest } from "../../middlewares/validation-middleware";
import { authenticateToken } from "../../middlewares/auth-middleware";
import { createTaskCommandSchema } from "../../../application/features/tasks/commands/create-task/create-task.command";
import { updateTaskCommandSchema } from "../../../application/features/tasks/commands/update-task/update-task.command";
import { deleteTaskCommandSchema } from "../../../application/features/tasks/commands/delete-task/delete-task.command";
import { getAllTasksQuerySchema } from "../../../application/features/tasks/queries/get-all-tasks/get-all-tasks.query";
import { getTaskQuerySchema } from "../../../application/features/tasks/queries/get-task/get-task.query";
import { z } from "zod";
import { resultToProblemDetails } from "../../../shared/result-to-problem";

export const tasksRoutes = Router();

const repository = taskRepository(db);

tasksRoutes.get(
    "/",
    authenticateToken,
    checkPermission({ resource: "tasks", action: "read" }),
    validate({
        query: getAllTasksQuerySchema,
    }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const userId = req.user?.id || "";
        const validatedQuery = req.validatedQuery!;

        console.log("🔵 [GET-TASKS] Query params:", { userId: validatedQuery.userId || userId, limit: validatedQuery.limit, offset: validatedQuery.offset });

        const result = await getAllTasks(repository, {
            userId: validatedQuery.userId || userId,
            limit: validatedQuery.limit,
            offset: validatedQuery.offset,
        });

        if (!result.ok) {
            console.log("🔴 [GET-TASKS] Error:", result.error);
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        console.log("✅ [GET-TASKS] Returning tasks:", result.data.length, "tasks");
        return res.status(200).json({
            data: result.data,
            total: result.data.length,
        });
    }
);

tasksRoutes.get(
    "/:id",
    authenticateToken,
    checkPermission({ resource: "tasks", action: "read" }),
    validate({ params: getTaskQuerySchema }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedParams = req.validatedParams!;

        const result = await getTask(repository, { id: validatedParams.id });

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(200).json({ data: result.data });
    }
);

tasksRoutes.post(
    "/",
    authenticateToken,
    checkPermission({ resource: "tasks", action: "create" }),
    validate({ body: createTaskCommandSchema.omit({ userId: true }) }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const userId = req.user?.id || "";
        const validatedData = req.validatedData!;

        const result = await createTask(repository, {
            ...validatedData,
            userId,
        });

        if (!result.ok) {
            const problem = resultToProblemDetails(result, req.originalUrl);
            return res.status(problem.status).json(problem);
        }

        return res.status(201).json({ data: result.data });
    }
);


tasksRoutes.put(
    "/:id",
    authenticateToken,
    checkPermission({ resource: "tasks", action: "update" }),
    validate({
        body: updateTaskCommandSchema.omit({ id: true }),
        params: z.object({ id: z.uuid() }),
    }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedParams = req.validatedParams;
        const validatedData = req.validatedData!;

        const result = await updateTask(repository, {
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


tasksRoutes.delete(
    "/:id",
    authenticateToken,
    checkPermission({ resource: "tasks", action: "delete" }),
    validate({ params: deleteTaskCommandSchema }),
    async (req: AuthenticatedRequest & ValidatedRequest, res: Response) => {
        const validatedParams = req.validatedParams!;

        const result = await deleteTask(repository, { id: validatedParams.id });

        if (!result.ok) {
            return res.status(result.error.code === "NOT_FOUND" ? 404 : 500).json({
                error: result.error.message,
                code: result.error.code,
            });
        }

        return res.status(204).send();
    }
);


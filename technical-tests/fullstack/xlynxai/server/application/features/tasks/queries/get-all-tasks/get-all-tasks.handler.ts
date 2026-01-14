import { ITaskRepository } from "../../../../../domain/interfaces/task-repository";
import { Result } from "../../../../../shared/result";
import { GetAllTasksQuery, GetAllTasksResult } from "./get-all-tasks.query";

export async function getAllTasks(
    taskRepository: ITaskRepository,
    query: GetAllTasksQuery
): Promise<GetAllTasksResult> {
    if (query.limit < 1 || query.limit > 100) {
        return Result.err("Limit must be between 1 and 100", "VALIDATION_ERROR");
    }

    if (query.offset < 0) {
        return Result.err("Offset must be greater than or equal to 0", "VALIDATION_ERROR");
    }

    const result = await taskRepository.list(query.userId || "", query.limit, query.offset);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}



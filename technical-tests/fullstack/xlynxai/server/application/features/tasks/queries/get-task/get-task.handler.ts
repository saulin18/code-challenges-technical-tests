import { ITaskRepository } from "../../../../../domain/interfaces/task-repository";
import { Result } from "../../../../../shared/result";
import { GetTaskQuery, GetTaskResult } from "./get-task.query";

export async function getTask(
    taskRepository: ITaskRepository,
    query: GetTaskQuery
): Promise<GetTaskResult> {
    const result = await taskRepository.getById(query.id);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}



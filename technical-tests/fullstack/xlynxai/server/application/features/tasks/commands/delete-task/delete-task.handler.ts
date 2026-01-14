import { ITaskRepository } from "../../../../../domain/interfaces/task-repository";
import { Result } from "../../../../../shared/result";
import { DeleteTaskCommand, DeleteTaskResult } from "./delete-task.command";

export async function deleteTask(
    taskRepository: ITaskRepository,
    command: DeleteTaskCommand
): Promise<DeleteTaskResult> {
    const existingTask = await taskRepository.getById(command.id);
    if (!existingTask.ok) {
        return Result.err("Task not found", "NOT_FOUND");
    }

    const result = await taskRepository.delete(command.id);

    if (!result.ok) {
        return result;
    }

    return Result.ok(undefined);
}


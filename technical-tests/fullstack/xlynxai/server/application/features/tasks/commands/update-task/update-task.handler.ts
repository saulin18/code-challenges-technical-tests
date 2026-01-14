import { ITaskRepository } from "../../../../../domain/interfaces/task-repository";
import { Task } from "../../../../../domain/entities/tasks";
import { Result } from "../../../../../shared/result";
import { UpdateTaskCommand, UpdateTaskResult } from "./update-task.command";

export async function updateTask(
    taskRepository: ITaskRepository,
    command: UpdateTaskCommand
): Promise<UpdateTaskResult> {
    
    const existingTaskResult = await taskRepository.getById(command.id);
    if (!existingTaskResult.ok) {
        return Result.err("Task not found", "NOT_FOUND");
    }

    const { id, ...updates } = command;
    const updateData = {
        id,
        ...Task.update(updates),
    };

    const result = await taskRepository.update(updateData);

    if (!result.ok) {
        return result;
    }

    return Result.ok(result.data);
}



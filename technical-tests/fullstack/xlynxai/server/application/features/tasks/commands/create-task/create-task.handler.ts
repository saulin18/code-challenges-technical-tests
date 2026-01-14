import { ITaskRepository } from "../../../../../domain/interfaces/task-repository";
import { Task } from "../../../../../domain/entities/tasks";
import { Result } from "../../../../../shared/result";
import { CreateTaskCommand, CreateTaskResult } from "./create-task.command";

export async function createTask(
    taskRepository: ITaskRepository,
    command: CreateTaskCommand
): Promise<CreateTaskResult> {
    try {
        console.log("🔵 [CREATE-TASK] Handler called with command:", JSON.stringify(command, null, 2));
  
    const assignedTo = command.assignedTo || command.userId;
        // statusId debe ser string vacío si no se proporciona (el tipo Task lo requiere)
        const statusId = command.statusId && command.statusId.trim() !== "" ? command.statusId : "";
    const startingTime = command.startingTime || new Date();
        // endingTime debe ser una fecha por defecto si no se proporciona (el tipo Task lo requiere)
    const endingTime = command.endingTime || new Date();

        console.log("🔵 [CREATE-TASK] Processed values:", { assignedTo, statusId, startingTime, endingTime });
  
    const newTask = Task.create({
        title: command.title,
        description: command.description,
        userId: command.userId,
        assignedTo,
        statusId,
        startingTime,
        endingTime,
    });

        console.log("🔵 [CREATE-TASK] Created task object:", JSON.stringify(newTask, null, 2));
   
    const result = await taskRepository.create(newTask);

    if (!result.ok) {
            console.log("🔴 [CREATE-TASK] Repository error:", result.error);
        return result;
    }

        console.log("✅ [CREATE-TASK] Task created successfully");
    return Result.ok(result.data);
    } catch (error) {
        console.log("🔴 [CREATE-TASK] Unexpected error:", error);
        return Result.err("Failed to create task", "INTERNAL_ERROR");
    }
}



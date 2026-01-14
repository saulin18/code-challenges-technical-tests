import { Result } from "../../common/result";
import { getApiUrl } from "../../common/api-config";
import { type Task } from "./types.ts";

interface ProblemDetails {
  status: number;
  title: string;
  detail?: string;
  type?: string;
  [key: string]: any;
}

interface ITaskService {
  getTasks: (
    userId: string,
    limit: number,
    offset: number
  ) => Promise<Result<{ data: Task[]; total: number }>>;
  createTask: (
    task: Omit<Task, "id" | "createdAt" | "updatedAt">
  ) => Promise<Result<Task>>;
  updateTask: (
    task: Required<Pick<Task, "id">> & Partial<Omit<Task, "id">>
  ) => Promise<Result<Task>>;
  deleteTask: (id: string) => Promise<Result<void>>;
  getTaskById: (id: string) => Promise<Result<Task>>;

  getTaskByUserId: (userId: string) => Promise<Result<Task[]>>;
}

export const taskService = (token: string): ITaskService => {
  return {
    getTasks: async (userId: string, limit: number, offset: number) => {
      const response = await fetch(
        getApiUrl(`/tasks?userId=${userId}&limit=${limit}&offset=${offset}`),
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      const data = await response.json();
      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to fetch tasks",
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }
      return Result.ok({ data: data.data, total: data.total });
    },
    getTaskById: async (id: string): Promise<Result<Task>> => {
      const response = await fetch(getApiUrl(`/tasks/${id}`), {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();
      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to fetch task",
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }
      return Result.ok(data.data);
    },
    getTaskByUserId: async (userId: string): Promise<Result<Task[]>> => {
      const response = await fetch(getApiUrl(`/tasks?userId=${userId}`), {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      const data = await response.json();
      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to fetch tasks",
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }
      return Result.ok(data.data);
    },
    createTask: async (
      task: Omit<Task, "id" | "createdAt" | "updatedAt">
    ): Promise<Result<Task>> => {
      // Convertir fechas a ISO strings y eliminar campos undefined
      const taskPayload: any = {
        title: task.title,
        description: task.description,
        userId: task.userId,
        startingTime: task.startingTime instanceof Date ? task.startingTime.toISOString() : task.startingTime,
      };
      
      // Solo agregar endingTime si existe
      if (task.endingTime) {
        taskPayload.endingTime = task.endingTime instanceof Date ? task.endingTime.toISOString() : task.endingTime;
      }
      
      // Solo agregar assignedTo si existe
      if (task.assignedTo) {
        taskPayload.assignedTo = task.assignedTo;
      }
      
      // Solo agregar statusId si existe
      if (task.statusId) {
        taskPayload.statusId = task.statusId;
      }
      
      console.log("🔵 [TASK-SERVICE] Creating task with payload:", JSON.stringify(taskPayload, null, 2));
      
      const response = await fetch(getApiUrl(`/tasks`), {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(taskPayload),
      });
      const data = await response.json();
      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to create task",
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }
      return Result.ok(data.data);
    },
    updateTask: async (
      task: Required<Pick<Task, "id">> & Partial<Omit<Task, "id">>
    ): Promise<Result<Task>> => {
      // Convertir fechas a ISO strings y eliminar campos undefined
      const taskPayload: any = {
        id: task.id,
      };
      
      if (task.title !== undefined) taskPayload.title = task.title;
      if (task.description !== undefined) taskPayload.description = task.description;
      if (task.assignedTo !== undefined) taskPayload.assignedTo = task.assignedTo;
      if (task.statusId !== undefined) taskPayload.statusId = task.statusId;
      if (task.endingTime !== undefined) {
        taskPayload.endingTime = task.endingTime instanceof Date 
          ? task.endingTime.toISOString() 
          : task.endingTime;
      }
      
      console.log("🔵 [TASK-SERVICE] Updating task with payload:", JSON.stringify(taskPayload, null, 2));
      
      const response = await fetch(getApiUrl(`/tasks/${task.id}`), {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(taskPayload),
      });
      const data = await response.json();
      if (!response.ok) {
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to update task",
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }
      return Result.ok(data.data);
    },
    deleteTask: async (id: string): Promise<Result<void>> => {
      const response = await fetch(getApiUrl(`/tasks/${id}`), {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (!response.ok) {
        const data = await response.json();
        const problem = data as ProblemDetails;
        return Result.err(
          problem.title || problem.detail || "Failed to delete task",
          problem.type || "UNKNOWN_ERROR",
          JSON.stringify({ status: problem.status || response.status })
        );
      }
      return Result.ok(undefined);
    },
  };
};

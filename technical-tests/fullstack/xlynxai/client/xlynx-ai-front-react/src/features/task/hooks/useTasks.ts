import { taskService } from "../task-service";
import { useInfiniteQuery, useMutation, useQuery } from "@tanstack/react-query";
import { type Task } from "../types";
import { useAuthContext } from "../../auth/auth-context";
import { throwResultError } from "../../../common/result";

export const useTasks = (limit: number) => {
  const { user, accessToken } = useAuthContext();
  const taskServiceInstance = taskService(accessToken);

  return useInfiniteQuery({
    
    queryKey: ["tasks", user?.id, limit],
    queryFn: async ({ pageParam = 0 }) => {
      const result = await taskServiceInstance.getTasks(user?.id || "", limit, pageParam);
      return throwResultError(result);
    },
    getNextPageParam: (lastPage, allPages) => {
      // Si la última página tiene menos items que el limit, no hay más páginas
      if (lastPage.data.length < limit) return undefined;
      // Retornar el siguiente offset
      return allPages.length * limit;
    },
    initialPageParam: 0,
    enabled: !!user?.id && !!accessToken,
  });
};

export const useCreateTask = () => {
  const { user, accessToken } = useAuthContext();
  const taskServiceInstance = taskService(accessToken);
  
  return useMutation({
    meta: {
      successMessage: "Task created successfully",
      errorMessage: "Failed to create task",
      invalidatesQuery: ["tasks", user?.id],
    },
    mutationFn: async (task: Omit<Task, "id" | "createdAt" | "updatedAt">) => {
      const result = await taskServiceInstance.createTask(task);
      return throwResultError(result);
    },
  });
};

export const useUpdateTask = () => {
  const { user, accessToken } = useAuthContext();
  const taskServiceInstance = taskService(accessToken);
  
  return useMutation({
    meta: {
      successMessage: "Task updated successfully",
      errorMessage: "Failed to update task",
      invalidatesQuery: ["tasks", user?.id],
    },
    mutationFn: async (task: Required<Pick<Task, "id">> & Partial<Omit<Task, "id">>) => {
      const result = await taskServiceInstance.updateTask(task);
      return throwResultError(result);
    },
  });
};

export const useDeleteTask = () => {
  const { user, accessToken } = useAuthContext();
  const taskServiceInstance = taskService(accessToken);
  
  return useMutation({
    meta: {
      successMessage: "Task deleted successfully",
      errorMessage: "Failed to delete task",
      invalidatesQuery: ["tasks", user?.id],
    },
    mutationFn: async (id: string) => {
      const result = await taskServiceInstance.deleteTask(id);
      return throwResultError(result);
    },
  });
};

export const useGetTaskById = (id: string) => {
  const { accessToken } = useAuthContext();
  const taskServiceInstance = taskService(accessToken);
  
  const { data, isLoading, error } = useQuery({
    queryKey: ["task", id],
    queryFn: async () => {
      const result = await taskServiceInstance.getTaskById(id);
      return throwResultError(result);
    },
    enabled: !!id && !!accessToken,
  });
  
  return { data, isLoading, error, taskService: taskServiceInstance };
};

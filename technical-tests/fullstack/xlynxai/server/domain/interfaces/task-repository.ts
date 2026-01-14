import { Task } from "../entities/tasks";
import { Result } from "../../shared/result";


export interface ITaskRepository {
    create: (task: Omit<Task, "id" | "createdAt" | "updatedAt">) => Promise<Result<Task>>;
    update: (task: Required<Pick<Task, "id">> & Partial<Omit<Task, "id">>) => Promise<Result<Task>>;
    //Soft delete
    delete: (id: string) => Promise<Result<void>>;
    getById: (id: string) => Promise<Result<Task>>;
    list: (userId: string, limit: number, offset: number) => Promise<Result<Task[]>>;
}
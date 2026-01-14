import { User } from "./user";


export type TaskStatus = {
    id: string;
    name: string;
}


export type Task = {

    id: string;
    title: string;
    description: string;

    // The user who created the task
    userId: User["id"];

    // The user who is assigned to the task
    assignedTo: User["id"];

    // The task status
    statusId: TaskStatus["id"];

    // When the task was created
    startingTime: Date;
    endingTime: Date;
    createdAt: Date;
    updatedAt: Date;

}

export const Task = {
    create: ({ title, description, startingTime, endingTime, userId, assignedTo, statusId }: Omit<Task, "id" | "createdAt" | "updatedAt">): Task => {
        return {
            id: crypto.randomUUID(),
            title,
            description,
            userId,
            assignedTo,
            statusId,
            startingTime,
            endingTime,
            createdAt: new Date(),
            updatedAt: new Date(),
        }
    },

    update: (updates: Partial<Pick<Task, "title" | "description" | "assignedTo" | "statusId" | "endingTime">>) => {
        return {
            ...updates,
            updatedAt: new Date(),
        }
    }
}
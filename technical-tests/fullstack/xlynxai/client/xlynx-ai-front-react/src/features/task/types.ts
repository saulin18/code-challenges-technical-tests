

export type Task = {
    id: string;
    title: string;
    description: string;
    startingTime: Date;
    endingTime: Date;
    userId: string;
    assignedTo: string;
    statusId: string;
}
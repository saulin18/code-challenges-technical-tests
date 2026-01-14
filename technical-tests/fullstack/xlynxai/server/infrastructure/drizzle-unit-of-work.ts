
import { AppDatabase } from "./database";
import { userRepository } from "./repositories/user-repository";
import { taskRepository } from "./repositories/task-repository";

export const drizzleUnitOfWork = (database: AppDatabase) => {
    return {
        startTransaction: async () => {
            return database.transaction(async (tx) => {
                return {
                    userRepository: userRepository(database, tx),
                    taskRepository: taskRepository(database, tx),
                }
            })
        },
        userRepository: userRepository(database),
        taskRepository: taskRepository(database),
    }
}
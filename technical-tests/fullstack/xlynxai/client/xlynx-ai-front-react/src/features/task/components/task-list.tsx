import { useEffect, useState } from 'react'
import type { Task } from '../types';
import TaskCard from './task-card';
import UpdateTaskDialog from './update-task-dialog';
import DeleteTaskDialog from './delete-task-dialog';
import CreateTaskDialog from './create-task-dialog';
import { useAuthContext } from '@/features/auth/auth-context';
import type { User } from '@/features/auth/types';
import { Button } from '@/common/components/ui/button';
import { useInView } from 'react-intersection-observer'

interface TasksListProps {
    tasks: Task[];
    onLoadMore: () => void;
}

function TasksList({ tasks, onLoadMore   }: TasksListProps) {
    const [taskToUpdate, setTaskToUpdate] = useState<Task | null>(null);
    const [taskToFinish, setTaskToFinish] = useState<Task | null>(null);
    const [taskToDelete, setTaskToDelete] = useState<Task | null>(null);
    const [openCreateTask, setOpenCreateTask] = useState<boolean>(false);

    const { ref, inView } = useInView({
        threshold: 0,
        rootMargin: '100px',
    });
    const { user } = useAuthContext();

    const handleUpdate = (task: Task) => {
        setTaskToUpdate(task);
    }

    const handleFinish = (task: Task) => {
        setTaskToFinish(task);
    }

    const handleCloseUpdate = () => {
        setTaskToUpdate(null);
    }

    const handleCloseFinish = () => {
        setTaskToFinish(null);
    }

    const handleDelete = (task: Task) => {
        setTaskToDelete(task);
    }

    const handleCloseDelete = () => {
        setTaskToDelete(null);
    }

    const handleOpenCreateTask = () => {
        setOpenCreateTask(true);
    }

    const handleCloseCreateTask = () => {
        setOpenCreateTask(false);
    }

    useEffect(() => {
        if (inView) {
            onLoadMore();
    }
    }, [inView, onLoadMore]);

    console.log(tasks)


    return (
        <>
            <main className='flex flex-col gap-4 p-4'>
                <Button onClick={handleOpenCreateTask}>Create Task</Button>
        <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4'>
            {tasks.map((task) => (
                        <TaskCard
                            key={task.id}
                            task={task}
                            onUpdate={handleUpdate}
                            onDelete={handleDelete}
                            onFinish={handleFinish}
                        />
            ))}
        </div>

                { /* div with the ref for the intersection observer */}
                <div ref={ref} className='h-10'></div>

                {/* Update Task Dialog */}
                {taskToUpdate && (
                    <UpdateTaskDialog
                        key={`update-${taskToUpdate.id}`}
                        task={taskToUpdate}
                        open={!!taskToUpdate}
                        onOpenChange={(open) => !open && handleCloseUpdate()}
                    />
                )}

                {/* Finish Task Dialog */}
                {taskToFinish && (
                    <UpdateTaskDialog
                        key={`finish-${taskToFinish.id}`}
                        task={taskToFinish}
                        open={!!taskToFinish}
                        onOpenChange={(open) => !open && handleCloseFinish()}
                        isForFinishTask={true}
                    />
                )}

                {/* Delete Task Dialog */}
                {taskToDelete && (
                    <DeleteTaskDialog
                        task={taskToDelete}
                        open={!!taskToDelete}
                        onOpenChange={(open) => !open && handleCloseDelete()}
                    />
                )}

                {/* Create Task Dialog */}
                {openCreateTask && (
                <CreateTaskDialog
                    open={openCreateTask}
                    onOpenChange={handleCloseCreateTask}
                        user={user as User}
                    />
                )}
            </main>
        </>
  )
}

export default TasksList
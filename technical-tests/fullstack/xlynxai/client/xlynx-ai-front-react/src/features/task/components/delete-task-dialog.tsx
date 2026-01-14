import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/common/components/ui/dialog'
import type { Task } from '../types';
import { useDeleteTask } from '../hooks/useTasks';
import { Button } from '@/common/components/ui/button';

interface DeleteTaskDialogProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
    task: Task;
}

function DeleteTaskDialog({ open, onOpenChange, task }: DeleteTaskDialogProps) {
    const { mutate: deleteTask, isPending } = useDeleteTask();
    
    const handleDeleteTask = () => {
        deleteTask(task.id, {
            onSuccess: () => {
                onOpenChange(false);
            }
        });
    }
    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Delete Task</DialogTitle>
                </DialogHeader>
                <DialogDescription>
                    Are you sure you want to delete the task "{task.title}"?
                </DialogDescription>
                <DialogFooter>
                    <Button onClick={handleDeleteTask} disabled={isPending}>
                        {isPending ? "Deleting..." : "Delete"}
                    </Button>
                    <Button variant="outline" onClick={() => onOpenChange(false)} disabled={isPending}>Cancel</Button>
                </DialogFooter>
            </DialogContent>
        </Dialog>
    )
}

export default DeleteTaskDialog
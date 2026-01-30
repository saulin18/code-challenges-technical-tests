import { Dialog, DialogContent, DialogFooter, DialogHeader, DialogTitle } from '@/common/components/ui/dialog'
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/common/components/ui/form'
import { Input } from '@/common/components/ui/input'
import { Button } from '@/common/components/ui/button'
import { Textarea } from '@/common/components/ui/textarea'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { useForm } from 'react-hook-form'
import { useUpdateTask } from '../hooks/useTasks'
import type { Task } from '../types'
import { Card, CardContent, CardHeader, CardTitle } from '@/common/components/ui/card'
import { useTaskElapsedTime } from '../hooks/useTaskElapsedTime';

export const updateTaskFormSchema = z.object({
    title: z.string().max(200).optional(),
    description: z.string().max(1000).optional(),
    assignedTo: z.uuid().optional().or(z.literal("")),
    statusId: z.uuid().optional().or(z.literal("")),
    endingTime: z.coerce.date().optional(),
});

type UpdateTaskFormData = z.infer<typeof updateTaskFormSchema>;

interface UpdateTaskDialogProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;

    task: Task;

    //If it's for finishing the task, the form will only update the ending time
    isForFinishTask?: boolean;
}

function UpdateTaskDialog({ open, onOpenChange, task, isForFinishTask = false }: UpdateTaskDialogProps) {
    const { mutate: updateTask, isPending } = useUpdateTask();

    const { elapsedTime, formatElapsedTime } = useTaskElapsedTime(task);

    const form = useForm<UpdateTaskFormData>({
        // @ts-expect-error - Zod v4 compatibility issue with @hookform/resolvers
        resolver: zodResolver(updateTaskFormSchema),
        defaultValues: isForFinishTask ? {
            endingTime: task.endingTime,
        } : {
            title: task.title,
            description: task.description,
            assignedTo: task.assignedTo,
            statusId: task.statusId,
        }
    })

    const onSubmit = (data: UpdateTaskFormData) => {
        const updateData: any = { id: task.id };
        
        if (isForFinishTask) {
            if (data.endingTime) {
                updateData.endingTime = data.endingTime;
            }
        } else {
            if (data.title) updateData.title = data.title;
            if (data.description) updateData.description = data.description;
            if (data.assignedTo && data.assignedTo !== "") updateData.assignedTo = data.assignedTo;
            if (data.statusId && data.statusId !== "") updateData.statusId = data.statusId;
            if (data.endingTime) updateData.endingTime = data.endingTime;
        }
        
        updateTask(updateData, {
            onSuccess: () => onOpenChange(false),
        });
    }
    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Update Task</DialogTitle>
                </DialogHeader>
                <Form {...form}>

                    {isForFinishTask ? (
                        <Card>
                            <CardHeader>
                                <CardTitle>Finish Task</CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-4">
                                <div className="text-center">
                                    <p className="text-sm text-muted-foreground mb-2">Elapsed Time</p>
                                    <p className="text-3xl font-mono font-bold">{formatElapsedTime(elapsedTime)}</p>
                                </div>
                                <form id="update-task-form" onSubmit={form.handleSubmit(onSubmit as any)}>
                                    <FormField
                                        control={form.control as any}
                                        name="endingTime"
                                        render={({ field }) => (
                                            <FormItem>
                                                <FormLabel>Ending Time</FormLabel>
                                                <FormControl>
                                                    <Input
                                                        type="datetime-local"
                                                        value={
                                                            field.value
                                                                ? new Date(field.value).toISOString().slice(0, 16)
                                                                : new Date().toISOString().slice(0, 16)
                                                        }
                                                        onChange={(e) => {
                                                            const dateValue = e.target.value ? new Date(e.target.value) : undefined;
                                                            field.onChange(dateValue);
                                                        }}
                                                    />
                                                </FormControl>
                                                <FormMessage />
                                            </FormItem>
                                        )}
                                    />
                                </form>
                            </CardContent>
                            <DialogFooter>
                                <Button
                                    type="submit"
                                    form="update-task-form"
                                    disabled={isPending}
                                >
                                    {isPending ? "Finishing..." : "Finish Task"}
                                </Button>
                            </DialogFooter>
                        </Card>
                    ) : (
                        <>
                            <Card>
                                <CardHeader>
                                    <CardTitle>Update Task</CardTitle>
                                </CardHeader>
                                <CardContent>
                                    <form 
                                        id="update-task-form" 
                                        onSubmit={form.handleSubmit(onSubmit as any)} 
                                        className="space-y-4"
                                    >
                                        <FormField
                                            control={form.control as any}
                                            name="title"
                                            render={({ field }) => (
                                                <FormItem>
                                                    <FormLabel>Title</FormLabel>
                                                    <FormControl>
                                                        <Input {...field} />
                                                    </FormControl>
                                                    <FormMessage />
                                                </FormItem>
                                            )}
                                        />
                                        <FormField
                                            control={form.control as any}
                                            name="description"
                                            render={({ field }) => (
                                                <FormItem>
                                                    <FormLabel>Description</FormLabel>
                                                    <FormControl>
                                                        <Textarea {...field} />
                                                    </FormControl>
                                                    <FormMessage />
                                                </FormItem>
                                            )}
                                        />
                                    </form>
                                </CardContent>
                            </Card>
                            <DialogFooter>
                                <Button
                                    type="submit"
                                    form="update-task-form"
                                    disabled={isPending}
                                >
                                    {isPending ? "Updating..." : "Update Task"}
                                </Button>
                            </DialogFooter>
                        </>
                    )}
                </Form>
            </DialogContent>
        </Dialog>
    );
}
export default UpdateTaskDialog;
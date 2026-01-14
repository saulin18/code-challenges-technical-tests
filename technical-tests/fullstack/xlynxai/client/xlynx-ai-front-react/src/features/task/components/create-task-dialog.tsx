import { Dialog, DialogContent, DialogHeader, DialogTitle } from '@/common/components/ui/dialog'
import { Form, FormField, FormItem, FormLabel, FormControl, FormMessage } from '@/common/components/ui/form'
import { Input } from '@/common/components/ui/input'
import { Button } from '@/common/components/ui/button'
import { Textarea } from '@/common/components/ui/textarea'
import { z } from 'zod'
import { zodResolver } from '@hookform/resolvers/zod'
import { useForm } from 'react-hook-form'
import { useCreateTask } from '../hooks/useTasks'
import type { User } from '@/features/auth/types'

export const createTaskFormSchema = z.object({
    title: z.string().min(1).max(200),
    description: z.string().min(1).max(1000),
    userId: z.uuid(),
    assignedTo: z.uuid().optional(),
    statusId: z.uuid().optional(),
    startingTime: z.coerce.date(),
    endingTime: z.coerce.date().optional(),
});

type CreateTaskFormData = z.infer<typeof createTaskFormSchema>;

interface CreateTaskDialogProps {
    open: boolean;
    onOpenChange: (open: boolean) => void;
    user: User;
}

function CreateTaskDialog({ open, onOpenChange, user }: CreateTaskDialogProps) {
    const { mutate: createTask, isPending } = useCreateTask();
    const form = useForm<CreateTaskFormData>({
        // @ts-expect-error - Zod v4 compatibility issue with @hookform/resolvers
        resolver: zodResolver(createTaskFormSchema),
        defaultValues: {
            title: '',
            description: '',
            startingTime: new Date(),
            endingTime: undefined,
            assignedTo: undefined,
            statusId: undefined,
            userId: user?.id,
        }
    })

    const onSubmit = (data: CreateTaskFormData) => {
        const taskData: any = {
            title: data.title,
            description: data.description,
            userId: data.userId,
            startingTime: data.startingTime,
        };

        // Solo agregar endingTime si existe
        if (data.endingTime) {
            taskData.endingTime = data.endingTime;
        }

        // Solo agregar assignedTo si existe y es diferente de userId
        if (data.assignedTo && data.assignedTo !== data.userId) {
            taskData.assignedTo = data.assignedTo;
        } 

        // Solo agregar statusId si existe y no está vacío
        if (data.statusId && data.statusId.trim() !== '') {
            taskData.statusId = data.statusId;
        }

        createTask(taskData);
        onOpenChange(false);
    }

    return (
        <Dialog open={open} onOpenChange={onOpenChange}>
            <DialogContent>
                <DialogHeader>
                    <DialogTitle>Create Task</DialogTitle>
                </DialogHeader>
                <Form {...form}>
                    <form id="create-task-form" onSubmit={form.handleSubmit(onSubmit as any)} className="space-y-4">
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
                        <Button type="submit" form="create-task-form" disabled={isPending}>
                            {isPending ? "Creating..." : "Create Task"}
                        </Button>
                    </form>
                </Form>
            </DialogContent>
        </Dialog>
    )
}

export default CreateTaskDialog;
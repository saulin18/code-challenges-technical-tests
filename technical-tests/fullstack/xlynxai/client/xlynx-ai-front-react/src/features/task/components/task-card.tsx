
import type { Task } from '../types'
import { Card, CardHeader, CardTitle, CardContent, CardFooter, CardDescription } from '@/common/components/ui/card'
import { Button } from '@/common/components/ui/button'
import { useTaskElapsedTime } from '../hooks/useTaskElapsedTime';

interface TaskCardProps {
    task: Task;
    onUpdate: (task: Task) => void;
    onDelete: (task: Task) => void;
    onFinish: (task: Task) => void;
}

function TaskCard({ task, onUpdate, onDelete, onFinish }: TaskCardProps) {

    const { elapsedTime, formatElapsedTime } = useTaskElapsedTime(task);

    return (
        <Card>
            <CardHeader>
                <CardTitle>{task.title}</CardTitle>
                <CardDescription>{task.description}</CardDescription>
            </CardHeader>
            <CardContent>
                <p className="text-sm text-muted-foreground mb-2">
                    Elapsed time: <span className="font-mono font-semibold">{formatElapsedTime(elapsedTime)}</span>
                </p>
            </CardContent>
            <CardFooter className="flex gap-2">
                <Button onClick={() => onUpdate(task)} variant="outline">Update Task</Button>
                <Button onClick={() => onDelete(task)} variant="destructive">Delete Task</Button>
                <Button onClick={() => onFinish(task)} variant="default">Finish Task</Button>
            </CardFooter>
        </Card>
    )
}

export default TaskCard
import { useTasks } from './hooks/useTasks';
import TasksList from './components/task-list';
import { useCallback } from 'react';

function TasksPage() {
    const limit = 10;
    const { 
        data, 
        fetchNextPage, 
        hasNextPage, 
        isFetchingNextPage 
    } = useTasks(limit);

    // Aplanar todas las páginas en un solo array
    const allTasks = data?.pages.flatMap(page => page.data) ?? [];

    const handleLoadMore = useCallback(() => {
        if (hasNextPage && !isFetchingNextPage) {
            fetchNextPage();
        }
    }, [hasNextPage, isFetchingNextPage, fetchNextPage]);

    return (
        <div className='p-4'>
            <TasksList tasks={allTasks} onLoadMore={handleLoadMore} />
        </div>
    );
}

export default TasksPage
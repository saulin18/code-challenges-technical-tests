
class MinHeap:
    def __init__(self, max_size):
        self.heap = []
        self.max_size = max_size
        self.current_size = 0
    

    def build_heap(self, arr):
        self.heap = arr
        self.current_size = len(arr)
        for i in range((self.current_size // 2) - 1, -1, -1):
            self.min_heapify(i)

    def is_leaf(self, index):
        return index >= (self.current_size // 2) and index < self.current_size

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def parent(self, index):
        return (index - 1) // 2

    def is_greater_than(self, index1, index2):
        assert 0 <= index1 < self.current_size, "Index1 out of bounds"
        assert 0 <= index2 < self.current_size, "Index2 out of bounds"
        return self.heap[index1] > self.heap[index2]

    def min_heapify(self, index):
        assert 0 <= index < self.current_size, "Index out of bounds"
        while not self.is_leaf(index):
            left = self.left_child(index)
            
            if left + 1 < self.current_size and self.is_greater_than(left, left + 1):
                left += 1

            if not self.is_greater_than(index, left):
                break

            self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
            index = left

    def move_up(self, index):
        assert 0 <= index < self.current_size, "Index out of bounds"
        while index > 0 and self.is_greater_than(self.parent(index), index):
            parent_index = self.parent(index)
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

        
    def insert(self, value):
        if self.current_size >= self.max_size:
            raise Exception("Heap is full")
        
        self.heap.append(value)
        self.current_size += 1
        self.move_up(self.current_size - 1)

    def remove_min(self):
        assert self.current_size > 0, "Heap is empty"
        min_value = self.heap[0]
        self.current_size -= 1  
        if self.current_size > 0:
            self.heap[0] = self.heap.pop()
            self.min_heapify(0)
            return min_value
        
        return self.heap.pop()
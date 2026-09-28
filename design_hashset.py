# 705. Design HashSet
# Design a HashSet without using any built-in hash table libraries.
# Implement MyHashSet class:
#     void add(key) Inserts the value key into the HashSet
#     bool contains(key) Returns whether the value key exists in the HashSet or not.
#     void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
# Example 1:
# Input
# ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]
# Output
# [null, null, null, true, false, null, true, null, false]

# Explanation
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1);      // set = [1]
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2);      // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2);   // set = [1]
# myHashSet.contains(2); // return False, (already removed)
# Constraints:


#     0 <= key <= 106
#     At most 104 calls will be made to add, remove, and contains.
class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next: "ListNode | None" = None


class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets: list[ListNode | None] = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key)
            return

        current = self.buckets[index]
        assert current is not None
        while current.next is not None:
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:

        if not self.contains(key):
            return

        index = self._hash(key)
        if self.buckets[index] is None:
            return

        current = self.buckets[index]
        assert current is not None

        if current.key == key:
            self.buckets[index] = current.next if current.next is not None else None
            return

        while current.next is not None and current.next.key != key:
            current = current.next

        assert current.next is not None
        current.next = current.next.next if current.next.next is not None else None
        return

    def contains(self, key: int) -> bool:
        if self.buckets[self._hash(key)] is not None:
            current = self.buckets[self._hash(key)]
            while current is not None:
                if current.key == key:
                    return True
                current = current.next
        return False
    
    
# class MyHashSet:

#     def __init__(self):
#         self.size = 1000
#         self.buckets = [[] for _ in range(self.size)]


#     def add(self, key: int) -> None:
#         idx = key % self.size
#         if key not in self.buckets[idx]:
#             self.buckets[idx].append(key)
#     def remove(self, key: int) -> None:
#         idx = key % self.size
#         if key not in self.buckets[idx]:
#             return
#         self.buckets[idx].remove(key)

#     def contains(self, key: int) -> bool:
#         idx = key % self.size
#         if key not in self.buckets[idx]:
#             return False
#         return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

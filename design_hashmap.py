# 706. Design HashMap
# Design a HashMap without using any built-in hash table libraries.
# Implement the MyHashMap class:
#     MyHashMap() initializes the object with an empty map.
#     void put(int key, int value) inserts a (key, value) pair into the HashMap.
# If the key already exists in the map, update the corresponding value.
#     int get(int key) returns the value to which the specified key is mapped,
# or -1 if this map contains no mapping for the key.
#     void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.
# Example 1:
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
# Constraints:

#     0 <= key, value <= 106
#     At most 104 calls will be made to put, get, and remove.

# Brute force approach
# class MyHashMap:

#     def __init__(self):
#         self.map: list[int | None] = [None for _ in range(1000001)]


#     def put(self, key: int, value: int) -> None:
#         self.map[key] = value

#     def get(self, key: int) -> int:
#         return self.map[key] if self.map[key] is not None else -1

#     def remove(self, key: int) -> None:
#         self.map[key] = None


# Chaining or bucket approach with Linked List
class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value: int = value
        self.next: "ListNode | None" = None


class MyHashMap:
    def __init__(self):
        self.size: int = 769
        self.buckets: list[ListNode | None] = [None] * self.size

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            assert current is not None
            while current is not None:

                if current.key == key:
                    current.value = value
                    return

                if current.next is None:
                    current.next = ListNode(key, value)
                    return

                current = current.next


    def get(self, key: int) -> int:
        index = self._hash(key)
        if self.buckets[index] is None:
            return -1
        else:
            current = self.buckets[index]
            assert current is not None
            while current is not None:
                if current.key == key:
                    return current.value
                else:
                    if current.next is None:
                        return -1
                    current = current.next
            return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if self.buckets[index] is None:
            return
        else:
            current = self.buckets[index]
            assert current is not None
            while current is not None:

                if current.key == key:
                    self.buckets[index] = (
                        current.next if current.next is not None else None
                    )
                    return

                if current.next is not None and current.next.key == key:
                    current.next.value = -1
                    current.next = (
                        current.next.next if current.next is not None else None
                    )
                    return

                current = current.next


# class MyHashMap:

# def __init__(self):
#     self.size = 769
#     self.bucket =[[] for _ in range(self.size)]

# def _hash(self, key):
#     return key % self.size


# def put(self, key: int, value: int) -> None:
#     idx = self._hash(key)
#     bucket = self.bucket[idx]
#     for i, (k, v) in enumerate(bucket):
#         if k == key:
#             bucket[i] = (key, value)
#             return
#     bucket.append((key, value))


# def get(self, key: int) -> int:
#     idx = self._hash(key)
#     bucket = self.bucket[idx]
#     for k,v in bucket:
#         if k == key:
#             return v
#     return -1


# def remove(self, key: int) -> None:
#     idx = self._hash(key)
#     bucket = self.bucket[idx]
#     for i, (k, v) in enumerate(bucket):
#         if k == key:
#             bucket.pop(i)
#             return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

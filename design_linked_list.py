# 707. Design Linked List
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
# and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in
# the linked list. Assume all nodes in the linked list are 0-indexed.
# Implement the MyLinkedList class:
#     MyLinkedList() Initializes the MyLinkedList object.
#     int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
#     void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion,
# the new node will be the first node of the linked list.
#     void addAtTail(int val) Append a node of value val as the last element of the linked list.
#     void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list.
# If index equals the length of the linked list, the node will be appended to the end of the linked list.
# If index is greater than the length, the node will not be inserted.
#     void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
# Example 1:
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
# Constraints:
#     0 <= index, val <= 1000
#     Please do not use the built-in LinkedList library.
#     At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
# When you insert with index < 0, test case will just treat as insert at index = 0.
# In order to pass test case(s) that require the solution to process values at a negative index:

#     on Get - treat negative index as zero if node list is empty
#     on AddAtIndex - insert element at index zero
from __future__ import annotations


class LLNode:
    val: int
    next: "LLNode | None"
    prev: "LLNode | None"

    def __init__(
        self, val: int, next: "LLNode | None" = None, prev: "LLNode | None" = None
    ):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head: 'LLNode | None' = None
        self.tail: 'LLNode | None' = None

    def get(self, index: int) -> int:
        last_index = 0

        if index == 0 and self.head is not None:
            return self.head.val

        if index < 0:
            return -1

        head = self.head
        while head is not None:
           

            if last_index == index:
                return head.val
            else:
                head = head.next
                last_index += 1

        return -1

    def addAtHead(self, val: int) -> None:
        old_head = self.head

        if old_head == None:
            new_head = LLNode(val, None, None)

            self.head = new_head
            self.tail = self.head
            return

        new_head = LLNode(val, None, None)
        self.head = new_head
        self.head.next = old_head
        old_head.prev = self.head
        return

    def addAtTail(self, val: int) -> None:
        old_tail = self.tail

        if old_tail == None:
            new_tail = LLNode(val, None, None)

            self.tail = new_tail
            self.head = self.tail
            return

        new_tail = LLNode(val, None, None)
        head = self.head
        assert head is not None, "head cant be None"

        old_tail.next = new_tail
        new_tail.prev = old_tail
        self.tail = new_tail
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        
        if index < 0:
            self.addAtHead(val)
            return

        current_index = 0
        head = self.head
        while head is not None:
           
            if current_index == index:
                prev_node = head.prev
                if prev_node is None:
                    return
                new_node = LLNode(val, head, prev_node)
                prev_node.next = new_node
                head.prev = new_node
                return
            head = head.next
            current_index += 1
        if current_index == index:
            self.addAtTail(val)
        return

    def deleteAtIndex(self, index: int) -> None:

        if index == 0:
            self.deleteAtHead()
            return

        current_index = 0
        head = self.head
        while head is not None:
         
            if current_index == index:
                prev_node = head.prev
                next_node = head.next
                if prev_node is not None:
                    prev_node.next = next_node
                else:
                    self.head = next_node
                if next_node is not None:
                    next_node.prev = prev_node
                else:
                    self.tail = prev_node
                return
            head = head.next
            current_index += 1
        return

    def deleteAtHead(self) -> None:
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

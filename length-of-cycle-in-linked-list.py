# 5 kyu
# Can you get the loop ?
# You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop.
# Your objective is to determine the length of the loop.

## Use the `next' attribute to get the following node
# node.next
# Notes:
# do NOT mutate the nodes!
# in some cases there can be just a loop, with no dangling piece.
# Don't miss dmitry's article in the discussion after you pass the Kata !!


def loop_size(node):
    exists_loop = False
    slow = node
    fast = node.next

    pointer_for_get_the_length = node
    counter = 0
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            exists_loop = True
            break

    pointer_for_get_the_length = fast.next     
    while exists_loop:
      
        if pointer_for_get_the_length == fast:
            return counter
        pointer_for_get_the_length = pointer_for_get_the_length.next
        counter += 1
        if pointer_for_get_the_length == fast:
            return counter

    return -1

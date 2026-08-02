from __future__ import annotations

# We will start with the node


# left will be childs[0] and right will be childs[1]
LEFT, RIGHT = 0, 1


class Node:
    def __init__(self, data):
        self.data = data
        self.color = 1  # 1 . Red, 0 . Black
        self.childs: list[Node | None] = [None, None]


root: Node | None = None


def is_red(node: Node | None) -> bool:
    if node is None:
        return False
    return node.color == 1

def is_black(node: Node | None) -> bool:
    if node is None:
        return True
    return node.color == 0

def flip_color(node: Node | None):
    if node is None:
        return
    for child in node.childs:
        if child is not None:
            child.color ^= 1
    node.color ^= 1


def rotate(node: Node, direction: int) -> Node:
    """Single rotation. direction=LEFT rotates left, direction=RIGHT rotates right."""
    opposite = 1 - direction
    new_root = node.childs[opposite]
    assert new_root is not None, "Cannot rotate: no child on the rotation side"
    node.childs[opposite] = new_root.childs[direction]
    new_root.childs[direction] = node

    new_root.color = node.color
    node.color = 1  # Red

    return new_root

def double_rotate(node: Node, direction: int) -> Node:
    """Align reds, then rotate."""
    opposite = 1 - direction
    child = node.childs[opposite]
    assert child is not None, "Cannot double rotate: no child on the rotation side"
    node.childs[opposite] = rotate(child, opposite)
    return rotate(node, direction)


def insert(data: int):
    global root
    root = __insert(root, data)
    root.color = 0  # Black

def __insert(node: Node | None, data: int) -> Node:
    if node is None:
        return Node(data)

    dir = 1 if data > node.data else 0  # left -> 0 , right -> 1

    node.childs[dir] = __insert(node.childs[dir], data)

    return insert_fix_up(node, dir)


def insert_fix_up(node: Node, dir: int) -> Node:
    opposite = 1 - dir

    if is_red(node.childs[dir]):
        child = node.childs[dir]
        assert child is not None

        if is_red(node.childs[opposite]):
            if is_red(child.childs[dir]) or is_red(child.childs[opposite]):
                flip_color(node)
        else:
            if is_red(child.childs[dir]):
                node = rotate(node, opposite)
            elif is_red(child.childs[opposite]):
                node = double_rotate(node, opposite)

    return node


def delete(data: int):
    global root
    if root is None:
        return
    root, _ = __delete(root, data)
    if root is not None:
        root.color = 0  # Black

def __delete(node: Node | None, data: int) -> tuple[Node | None, bool]:
    """Returns (new subtree root, ok). ok=True means the black-height of this
    subtree is unchanged, so nothing further needs fixing up the call stack."""

    if node is None:
        return None, True

    if node.data == data:
        if node.childs[LEFT] is None and node.childs[RIGHT] is None:
            # Leaf: removing a red leaf is free, removing a black one
            # shortens this path by one black node.
            return None, is_red(node)

        if node.childs[LEFT] is None or node.childs[RIGHT] is None:
            # Exactly one child: by the RB invariants that child must be red
            # and this node must be black, so absorbing it is always safe.
            child = node.childs[LEFT] if node.childs[LEFT] is not None else node.childs[RIGHT]
            assert child is not None
            child.color = 0  # Black
            return child, True

        # Two children: replace with the in-order predecessor (max of left subtree)
        left = node.childs[LEFT]
        assert left is not None
        temp = get_max(left)
        node.data = temp.data
        data = temp.data

    dir = 1 if data > node.data else 0
    new_child, ok = __delete(node.childs[dir], data)
    node.childs[dir] = new_child

    if ok:
        return node, True
    return delete_fix_up(node, dir)

def get_max(node: Node) -> Node:
    """Get the maximum node in the subtree rooted at the given node."""
    current = node
    while True:
        next_node = current.childs[RIGHT]
        if next_node is None:
            return current
        current = next_node

def delete_fix_up(node: Node, dir: int) -> tuple[Node, bool]:
    """node is the parent of the subtree that just got one black node
    shorter on its `dir` side."""
    opposite = 1 - dir
    new_root = node
    sibling = node.childs[opposite]

    if is_red(sibling):
        new_root = rotate(node, dir)  # promotes sibling; `node` becomes new_root.childs[dir]
        sibling = node.childs[opposite]

    assert sibling is not None, "Sibling can't be None here without breaking black-height"

    if is_black(sibling.childs[LEFT]) and is_black(sibling.childs[RIGHT]):
        sibling.color = 1  # Red
        if is_red(node):
            node.color = 0  # Black
            return new_root, True
        return new_root, False

    if is_black(sibling.childs[opposite]):
        # Near nephew red, far nephew black: realign so the far side is red.
        node.childs[opposite] = rotate(sibling, opposite)

    old_color = node.color
    promoted = rotate(node, dir)
    promoted.color = old_color
    promoted_left, promoted_right = promoted.childs[LEFT], promoted.childs[RIGHT]
    assert promoted_left is not None and promoted_right is not None
    promoted_left.color = 0  # Black
    promoted_right.color = 0  # Black

    if new_root is node:
        new_root = promoted
    else:
        new_root.childs[dir] = promoted

    return new_root, True



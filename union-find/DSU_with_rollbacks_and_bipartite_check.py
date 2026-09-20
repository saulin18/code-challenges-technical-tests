
from typing import Annotated, cast

Roots = Annotated[tuple[int, int], 2]
OldColorY = Annotated[int, 1]
WasBipartite = Annotated[bool, 1]
WasMerged = Annotated[bool, 1]
StackParams = Annotated[tuple[Roots, OldColorY, WasBipartite, WasMerged], 4]


class DSU_with_rollbacks_and_bipartite_check:
    def __init__(self, n):
        self.parent = list(range(n))

        self.size = [1] * n
        self.stack: list[StackParams] = []
        self.comps = n
        self.sentinel = -1
        self.is_bipartite = True
        self.color = [0] * n

    def find(self, x: int) -> tuple[int, int]:
        parent = x
        parity = 0
        while self.parent[parent] != parent:
            parity ^= self.color[parent]
            parent = self.parent[parent]

        return parent, parity

    def union(self, x: int, y: int):
        x, parity_x = self.find(x)
        y, parity_y = self.find(y)

        if x == y:
            is_bipartite = parity_x != parity_y
            if not is_bipartite:
                self.stack.append(
                    cast(StackParams, ((x, y), self.color[y], self.is_bipartite, False))
                )
                self.is_bipartite = False
            return

        if self.size[x] < self.size[y]:
            x, y = y, x
            parity_x, parity_y = parity_y, parity_x
        self.parent[y] = x
        
        previous_y_color = self.color[y]
        
        self.color[y] = parity_x ^ parity_y ^ 1
        self.size[x] += self.size[y]
        self.stack.append(
            cast(StackParams, ((x, y), previous_y_color, self.is_bipartite, True))
        )
        self.comps -= 1
        

    def get_comps(self):
        return self.comps

    def persist(self):
        self.stack.append(
            cast(StackParams, ((self.comps, self.sentinel), 0, self.is_bipartite, False))
        )

    def rollback_to_previous_state(self):
        """
        Rollback to the previous state before the last persist.
        """
        if len(self.stack) == 0:
            raise ValueError("No previous state to rollback to")
        while self.stack[-1][0][1] != self.sentinel:
            roots, old_color_y, was_bipartite, was_merged = self.stack.pop()
            x, y = roots
            if not was_merged:
                self.is_bipartite = was_bipartite
                continue
            
            x, y = roots
            
            self.parent[y] = y
            self.color[y] = old_color_y
            self.size[x] -= self.size[y]
            self.is_bipartite = was_bipartite
            self.comps += 1
        self.stack.pop()

    def rollback(self, k: int):
        """
        Rollback the last k operations.
        Args:
            k (int): The number of operations to rollback.

        Raises:
            ValueError: If there are not enough operations to rollback.
        """
        if len(self.stack) < k:
            raise ValueError("Not enough operations to rollback")

        for _ in range(k):
            roots, old_color_y, was_bipartite, was_merged = self.stack.pop()
            
            if not was_bipartite:
                self.is_bipartite = False
                continue
            
            x, y = roots
            self.parent[y] = y
            self.size[x] -= self.size[y]
            self.color[y] = old_color_y
            self.is_bipartite = was_bipartite
            self.comps += 1

    def get_size(self, x: int) -> int:
        return self.size[self.find(x)[0]]

    def get_parent(self, x: int) -> int:
        return self.parent[self.find(x)[0]]

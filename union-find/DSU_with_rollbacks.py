class DSU_with_rollbacks:
    def __init__(self, n):
        self.parent = list(range(n))

        self.size = [1] * n
        self.stack: list[tuple[int, int]] = []
        self.comps = n
        self.sentinel = -1

    def find(self, x):
        parent = x
        while self.parent[parent] != parent:
            parent = self.parent[parent]
        return parent

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.stack.append((x, y))
        self.comps -= 1

    def get_comps(self):
        return self.comps

    def persist(self):
        self.stack.append((self.comps, self.sentinel))

    def rollback_to_previous_state(self):
        """
        Rollback to the previous state before the last persist.
        """
        if len(self.stack) == 0:
            raise ValueError("No previous state to rollback to")
        while self.stack[-1][1] != self.sentinel:
            x, y = self.stack.pop()
            self.parent[y] = y
            self.size[x] -= self.size[y]
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
            x, y = self.stack.pop()
            self.parent[y] = y
            self.size[x] -= self.size[y]
            self.comps += 1

    def get_size(self, x):
        return self.size[self.find(x)]

    def get_parent(self, x):
        return self.parent[self.find(x)]



import collections
import random
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from itertools import chain, count, dropwhile, repeat
from threading import Lock


def geometric(p):
    return (next(dropwhile(lambda _: random.randint(1, int(1. / p)) == 1, count())) for _ in repeat(1))


# Simple deterministic distribution for testing internals of the skiplist. 
uniform = repeat



class NIL:
    """Sentinel object that always compares greater than another object"""
    __slots__ = ()

    def __cmp__(self, other):
        # NIL is always greater than the other
        return 1

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __ge__(self, other):
        return True

    def __str__(self):
        return 'NIL'

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False


class _Skipnode:
    __slots__ = ('data', 'height', 'key', 'nxt', 'prev')

    def __init__(self, key, data, nxt, prev):
        self.key = key
        self.data = data
        self.nxt = nxt
        self.prev = prev

        for level in range(len(prev)):
            prev[level].nxt[level] = self.nxt[level].prev[level] = self


class LockableArray(list):
    def __init__(self, seq=()):
        super().__init__(seq)
        self._lock = Lock()

    @contextmanager
    def lock(self):
        try:
            yield self._lock.acquire()
        finally:
            self._lock.release()


class SkiplistAbstractBase:
    __metaclass__ = ABCMeta
    """Class for randomized indexed skip list. The default
    distribution of node heights is geometric."""

    distribution = geometric(0.5)

    @property
    @abstractmethod
    def head(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def tail(self):
        raise NotImplementedError

    def _height(self):
        return len(self.head.nxt)

    def _level(self, start=None, level=0):
        node = start or self.head.nxt[level]
        while node is not self.tail:
            yield node
            node = node.nxt[level]

    def _scan(self, key):
        return_value = None
        height = len(self.head.nxt)
        prevs = LockableArray([self.head] * height)
        node = self.head.nxt[-1]
        for level in reversed(range(height)):
            node = next(
                dropwhile(
                    lambda node_: node_.nxt[level].key <= key,  # noqa: B023
                    chain([self.head], self._level(node, level))
                )
            )
            if node.key == key:
                return_value = node
            else:
                prevs[level] = node

        return return_value, prevs

    def _insert(self, key, data):
            """Inserts data into appropriate position."""

            node, update = self._scan(key)

            if node:
                node.data = data
                return

            node_height = next(self.distribution) + 1  # because height should be positive non-zero
            # if node's height is greater than number of levels
            # then add new levels, if not do nothing
            height = len(self.head.nxt)

            update.extend([self.head for _ in range(height, node_height)])

            self.head.nxt.extend([self.tail for _ in range(height, node_height)])

            self.tail.prev.extend([self.head for _ in range(height, node_height)])

            _Skipnode(key, data, [update[l].nxt[l] for l in range(node_height)], [update[l] for l in range(node_height)])

    def _remove(self, key):
        """Removes node with given data. Raises KeyError if data is not in list."""

        node, update = self._scan(key)
        if not node:
            raise KeyError

        with update.lock():
            for level in range(len(node.nxt)):
                update[level].nxt[level] = node.nxt[level]

        # trim not used head pointers
        for i in reversed(range(len(self.head.nxt))):
            if self.head.nxt[i] != self.tail:
                break
            elif i > 0:  # at least one pointer
                head_node = self.head.nxt.pop()
                del head_node

        del node


class Skiplist(SkiplistAbstractBase, collections.abc.MutableMapping):

    def _remove(self, key):
        super()._remove(key)
        self._size -= 1

    def _insert(self, key, data):
        super()._insert(key, data)
        self._size += 1

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __init__(self, **kwargs):
        super().__init__()

        self._tail = _Skipnode(NIL(), None, [], [])
        self._head = _Skipnode(None, 'HEAD', [self.tail], [])
        self._tail.prev.extend([self.head])

        self._size = 0

        for k, v in kwargs.items():
            self[k] = v

    def __len__(self):
        return self._size

    def __str__(self):
        return 'skiplist({{{}}})'.format(
            ', '.join(f'{node.key}: {node.data}' for node in self._level())
        )

    def __getitem__(self, key):
        """Returns item with given index"""
        node, _ = self._scan(key)
        if node is None:
            raise KeyError(f'Key <{key}> not found')
        return node.data

    def __setitem__(self, key, value):
        return self._insert(key, value)

    def __delitem__(self, key):
        self._remove(key)

    def __iter__(self):
        """Iterate over keys in sorted order"""
        return (node.key for node in self._level())

    def iteritems(self):
        return ((node.key, node.data) for node in self._level())

    def iterkeys(self):
        return (item[0] for item in self.iteritems())

    def itervalues(self):
        return (item[1] for item in self.iteritems())



# import random
# import threading
# from collections.abc import MutableMapping


# class _Node:
#     __slots__ = ('key', 'value', 'forward')

#     def __init__(self, key, value, level):
#         self.key = key
#         self.value = value
#         self.forward = [None] * level


# class Skiplist(MutableMapping):
#     """Simple skip list backed dict.

#     Only mutating operations (insert/delete) take the lock — reads walk
#     the forward pointers without one, which is safe under the GIL but not
#     linearizable against a concurrent write.
#     """

#     def __init__(self, max_level=16, promotion_probability=0.5, **kwargs):
#         self._max_level = max_level
#         self._promotion_probability = promotion_probability
#         self._level = 1
#         self._size = 0
#         self._head = _Node(None, None, max_level)
#         self._lock = threading.Lock()

#         for key, value in kwargs.items():
#             self[key] = value

#     def _random_level(self):
#         level = 1
#         while level < self._max_level and random.random() < self._promotion_probability:
#             level += 1
#         return level

#     def _find_update_path(self, key):
#         """Returns, per level, the last node whose key is < key."""
#         update = [self._head] * self._max_level
#         node = self._head
#         for level in reversed(range(self._level)):
#             while node.forward[level] is not None and node.forward[level].key < key:
#                 node = node.forward[level]
#             update[level] = node
#         return update

#     def __getitem__(self, key):
#         update = self._find_update_path(key)
#         node = update[0].forward[0]
#         if node is None or node.key != key:
#             raise KeyError(key)
#         return node.value

#     def __setitem__(self, key, value):
#         with self._lock:
#             update = self._find_update_path(key)
#             node = update[0].forward[0]

#             if node is not None and node.key == key:
#                 node.value = value
#                 return

#             level = self._random_level()
#             if level > self._level:
#                 for i in range(self._level, level):
#                     update[i] = self._head
#                 self._level = level

#             new_node = _Node(key, value, level)
#             for i in range(level):
#                 new_node.forward[i] = update[i].forward[i]
#                 update[i].forward[i] = new_node

#             self._size += 1

#     def __delitem__(self, key):
#         with self._lock:
#             update = self._find_update_path(key)
#             node = update[0].forward[0]

#             if node is None or node.key != key:
#                 raise KeyError(key)

#             for i in range(self._level):
#                 if update[i].forward[i] is not node:
#                     break
#                 update[i].forward[i] = node.forward[i]

#             while self._level > 1 and self._head.forward[self._level - 1] is None:
#                 self._level -= 1

#             self._size -= 1

#     def __contains__(self, key):
#         update = self._find_update_path(key)
#         node = update[0].forward[0]
#         return node is not None and node.key == key

#     def __iter__(self):
#         node = self._head.forward[0]
#         while node is not None:
#             yield node.key
#             node = node.forward[0]

#     def __len__(self):
#         return self._size

#     def __str__(self):
#         return 'skiplist({{{}}})'.format(
#             ', '.join('{}: {}'.format(k, v) for k, v in self.items())
#         )

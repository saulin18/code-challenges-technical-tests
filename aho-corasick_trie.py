from __future__ import annotations


# Implementation of the Aho-corasick algorithm for string matching
class TrieNode:
    def __init__(self):
        self.children: list["TrieNode | None"] = [None for _ in range(26)]
        self.is_end_of_word: bool = False
        self.parent: "TrieNode | None" = None
        self.created_at_char_index: int = -1
        self.suffix_link: "TrieNode | None" = None
        self.go_to: list["TrieNode | None"] = [None for _ in range(26)]

    def insert(self, key: str) -> None:

        n = len(key)
        root = self
        if root is None:
            return
        for i in range(n):
            index_in_trie = ord(key[i]) - ord("a")

            assert root is not None, "root cant be None"
            if root.children[index_in_trie] is None:
                parent = root
                newNode = TrieNode()
                newNode.parent = parent
                newNode.created_at_char_index = index_in_trie
                root.children[index_in_trie] = newNode

            root = root.children[index_in_trie]

        assert root is not None, "root cant be None"
        root.is_end_of_word = True

    def get_suffix_link(self) -> TrieNode | None:
        if self.suffix_link is not None:
            return self.suffix_link
        # node is root
        if self.parent is None:
            self.suffix_link = self
            return self.suffix_link

        if self.parent.parent is None:
            self.suffix_link = self.parent
            return self.suffix_link
        self.suffix_link = self.go(
            self.parent.get_suffix_link(), self.created_at_char_index
        )
        return self.suffix_link

    def go(self, node: TrieNode | None, char_index: int) -> TrieNode | None:
        if node is None:
            return None
        if node.go_to[char_index] is not None:
            return node.go_to[char_index]

        if node.children[char_index] is not None:
            node.go_to[char_index] = node.children[char_index]
            return node.go_to[char_index]
        if node.parent is None:
            node.go_to[char_index] = node
            return node.go_to[char_index]
        node.go_to[char_index] = node.go(node.get_suffix_link(), char_index)
        return node.go_to[char_index] if node.go_to[char_index] is not None else node


def do_aho_corasick(m: str, n: str) -> bool:

    trie = TrieNode()

    trie.insert(n)

    length = len(m)
    for i in range(length):
        char = m[i]
        index = ord(char) - ord("a")
        assert trie is not None
        trie = trie.go(trie, index)
        if trie is None:
            continue
        if trie.is_end_of_word:
            return True
        
        # Support for search in multiple words
        # link = trie.get_suffix_link()
        # while link is not None and link.parent is not None:
        #     if link.is_end_of_word:
        #         return True
        #     link = link.get_suffix_link()

    return False

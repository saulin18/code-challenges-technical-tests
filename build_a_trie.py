# Build a Trie
# The goal of this kata is to implement trie (or prefix tree) using dictionaries
# (aka hash maps or hash tables), where:
# the dictionary keys are the prefixes
# the value of a leaf node is None in Python, nil in Ruby, null in Groovy,
# JavaScript and Java, and Nothing in Haskell.
# the value for empty input is {} in Python, Ruby, Javascript and Java
# (empty map), [:] in Groovy, and Trie [] in Haskell.
# Examples:
# >>> build_trie()
# {}
# >>> build_trie("")
# {}
# >>> build_trie("trie")
# {'t': {'tr': {'tri': {'trie': None}}}}
# >>> build_trie("tree")
# {'t': {'tr': {'tre': {'tree': None}}}}
# >>> build_trie("A","to", "tea", "ted", "ten", "i", "in", "inn")
# {'A': None, 't': {'to': None, 'te': {'tea': None, 'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}}
# >>> build_trie("true", "trust")
# {'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}}
# Happy coding! :)


class Trie:
    def __init__(self):
        self.children: dict[str, "Trie"] = {}
        self.is_end_of_word: bool = False

    def insert(self, word: str):
        trie = self
        for char in word:
            if char not in trie.children:
                trie.children[char] = Trie()
                trie = trie.children[char]
                continue
            trie = trie.children[char]
        trie.is_end_of_word = True
        return

    def to_dict(self, prefix: str, res: dict, trie: "Trie") -> dict:

        if prefix is None:
            return

        for char, new_trie in trie.children.items():
            new_prefix = prefix + char
            if new_trie.is_end_of_word:
                res[new_prefix] = None

                if not new_trie.children:
                    res[new_prefix] = None
                else:
                    res[new_prefix] = {}

                self.to_dict(new_prefix, res[new_prefix], new_trie)
            
            if not new_trie.is_end_of_word:
                res[new_prefix] = {}
                self.to_dict(new_prefix, res[new_prefix], new_trie)

        return res


def build_trie(*words: str) -> dict:

    new_trie = Trie()

    for word in words:
        new_trie.insert(word)

    return new_trie.to_dict("", {}, new_trie)

# def build_trie(*words):
#     root = {}
#     for word in words:
#         branch = root
#         length = len(word)
#         for i in range(1, length+1):
#             length -= 1
#             key = word[:i]
#             if key not in branch: 
#                 branch[key] = None
#             if length and not branch[key]: 
#                 branch[key] = {}
#             branch = branch[key]
#     return root
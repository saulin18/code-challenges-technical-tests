# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a string. The encoded string
# is then sent over the network and is decoded back to the original list of strings.
# Machine 1 (sender) has the function:
# string encode(vector<string> strs) {
#     // ... your code
#     return encoded_string;
# }
# Machine 2 (receiver) has the function:
# vector<string> decode(string s) {
#     //... your code
#     return strs;
# }
# So Machine 1 does:
# string encoded_string = encode(strs);
# and Machine 2 does:
# vector<string> strs2 = decode(encoded_string);
# strs2 in Machine 2 should be the same as strs in Machine 1.
# Implement the encode and decode methods.
# Example 1:
# Input: dummy_input = ["Hello","World"]
# Output: ["Hello","World"]
# Explanation:
# Machine 1:
# Codec encoder = new Codec();
# String msg = encoder.encode(strs);
# Machine 1 ---msg---> Machine 2
# Machine 2:
# Codec decoder = new Codec();
# String[] strs = decoder.decode(msg);
# Example 2:
# Input: dummy_input = [""]
# Output: [""]
# Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.
# Follow up: Could you write a generalized algorithm to
# work on any possible set of characters?

from typing import List


class Solution:
    SEP = "-#"

    def encode(self, strs: List[str]) -> str:
        sep = self.SEP
        return "".join(f"{len(w)}{sep}{w}" for w in strs)

    def decode(self, s: str) -> List[str]:
        separator = "-#"
        res = []

        last_duration_of_word = 0
        block_start = 0
        for i, char in enumerate(s):
            if last_duration_of_word != 0:
                last_duration_of_word -= 1
                continue

            if char == separator[-1] and s[i - 1] == separator[-2]:
                length = int(s[block_start : i - 1])
                end_index = i + length + 1
                word = s[i + 1 : end_index]
                res.append(word)
                last_duration_of_word = length
                block_start = end_index

        return res

#557. Reverse Words in a String III
#
#Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
#Example 1:
#
#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
#Example 2:
#
#Input: s = "Mr Ding"
#Output: "rM gniD"

def reverseWords(self, s):
        
     words = s.split(' ')
     
     reversed_words = []  
     
     for word in words:
         reversed_words.append(word[::-1])
     
     return " ".join(reversed_words)     
 
# def reverseWords(self, s):
#  return " ".join([word[::-1] for word in s.split()])


# def reverseWords(self, s):
# return " ".join(map(lambda word: word[::-1], s.split()))

# def reverseWords(self, s):
#    return " ".join("".join(reversed(word)) for word in s.split())

#def reverseWords(self, s):
#    words = s.split()
#    reversed_words = [word[::-1] for word in words]
#    return " ".join(reversed_words)

#import re
#
#def reverseWords(self, s):
#    return re.sub(r'\S+', lambda m: m.group()[::-1], s)

#from functools import reduce
##
#def reverseWords(self, s):
#    return " ".join(reduce(lambda acc, word: acc + [word[::-1]], s.split(), []))
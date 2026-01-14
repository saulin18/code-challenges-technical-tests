#Instructions
#Output
#Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.
#
#Example:
#
#Given an input string of:
#
#apples, pears # and bananas
#grapes
#bananas !apples
#The output expected would be:
#
#apples, pears
#grapes
#bananas

def strip_comments(strng: str, markers: list[str]):
    
    words = strng.strip().split('\n')
    print(words)

    for i in range(len(words)):
        for marker in markers: 
            if words[i].find(marker) != -1:
                words[i] = words[i][:words[i].find(marker)].rstrip()
                break
    
    return "\n".join(words).strip()        
    
print(strip_comments('apples, pears # and bananas', ["#"]) )   


def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
# 👹 The Grinch's attack
# The Grinch 👹 has passed through Santa Claus's workshop! And what a mess he has made. He has changed the order
# of some
# packages, so shipments cannot be made.
# Luckily, the elf Pheralb has detected the pattern the Grinch followed to jumble them. He has written the rules that 
# we must follow to reorder the packages. The instructions are as follows:

# You will receive a string containing letters and parentheses. Every time you find a pair of parentheses, you need 
# to reverse the content within them. If there are nested parentheses, solve the innermost ones first. 
# Return the resulting string with parentheses removed, but with the content correctly reversed. 

# fixPackages("a(cb)de");
# // ➞ "abcde"
# // We reverse "cb" inside the parentheses
# fixPackages("a(bc(def)g)h");
# // ➞ "agdefcbh"
# // 1st we reverse "def" → "fed", then we reverse "bcfedg" → "gdefcb"
# fixPackages("abc(def(gh)i)jk");
# // ➞ "abcighfedjk"
# // 1st we reverse "gh" → "hg", then "defhgi" → "ighfed" 
# fixPackages("a(b(c))e");
# // ➞ "acbe"
# // 1st we reverse "c" → "c", then "bc" → "cb"

def fix_packages(packages: str) -> str:
    
    if not packages:
        return ""
    
    l = -1
    r = -1
    
    def reverse_between(l, r):
        return packages[:l] + packages[l:r][::-1] + packages[r:]
    
    for i, char in enumerate(packages):
        if char == "(":
            l = i
        elif char == ")":
            r = i
            
            if l != -1 and r != -1:
                aux = reverse_between(l, r)
                new_packages = aux.replace("(", "").replace(")", "")
                packages = new_packages[::]
                l = -1
                r = -1

    return packages

#print(fix_packages("a(cb)de"))
print(fix_packages("a(bc(def)g)h"))
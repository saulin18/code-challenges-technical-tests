# 📦 Is the gift inside the box?

# We have already wrapped hundreds of presents 🎁… but an elf forgot to check if the present, 
# represented by an asterisk *, is inside the box.
# The box has a present (*) and counts as "inside the box" if: 
# - It is completely surrounded by # on the box's edges.
# - The * is not on the box's edges.
# Keep in mind that the * can be inside, outside, or may not even be there. 
# We must return true if the * is inside the box and false otherwise.
# Examples:
# inBox([
#   "###",
#   "#*#",
#   "###"
# ]); // ➞ true
# inBox([
#   "####",
#   "#* #",
#   "#  #",
#   "####"
# ]); // ➞ true
# inBox([
#   "#####",
#   "#   #",
#   "#  #*",
#   "#####"
# ]); // ➞ false
# inBox([
#   "#####",
#   "#   #",
#   "#   #",
#   "#   #",
#   "#####"
# ]); // ➞ false

def in_box(box: list[str]) -> bool:
    
    if not box:
        return False
    
    for i, row in enumerate(box):
        # The first and last row are the edges of the box, the gift isnt in the edges
        if i == 0 or i == len(box) - 1:
            continue
        
        if (pos := row.find("*")) != -1:
            return pos > 0 and pos < len(row) - 1
        
    return False

print(in_box([
    "###",
    "#*#",
    "###"
]))
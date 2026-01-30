# 🖼️ Framing names
# Santa Claus 🎅 wants to frame the names of the good children to decorate his workshop 🖼️, 
# but the frame must follow specific rules. Your task is to help the elves generate this magical frame.
# Rules:
# Given an array of names, you must create a rectangular frame that contains all of them.
# Each name must be on a line, aligned to the left.
# The frame is built with * and has a border one line thick.
# The width of the frame automatically adapts to the longest name plus a margin of 1 space on each side.
# Example of how it works:
# createFrame(['midu', 'madeval', 'educalvolpz'])
# // Expected result:
# ***************
# * midu        *
# * madeval     *
# * educalvolpz *
# ***************
# createFrame(['midu']
# // Expected result:
# ********
# * midu *
# ********
# createFrame(['a', 'bb', 'ccc'])
# // Expected result:
# *******
# * a   *
# * bb  *
# * ccc *
# *******
# createFrame(['a', 'bb', 'ccc', 'dddd'])


from typing import List


def create_frame(list_of_frames: List[str]) -> str:
    
    longest_frame_length = len(max(list_of_frames, key=len))
    
    # The total length of the first line and the last is the length of the longest frame * 2
    first_line = "*" * (longest_frame_length * 2)
    endline = first_line[::]
    
    # Rows arr
    rows = []    
    rows.append(first_line)
    
    length_of_each_row = longest_frame_length 
    
    for frame in list_of_frames:
        # I'd use a function but meh
        row = "* " + frame + " " * (length_of_each_row - len(frame)) + " *"
        
        
        rows.append(row)
        
    rows.append(endline)    
    return "\n".join(rows)    

print(create_frame(['a', 'bb', 'ccc', 'dddd']))
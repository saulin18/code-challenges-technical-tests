# 1. Read Entire File
#
# Write a Python program to read an entire text file.


def read_entire_file():
    with open("files/data.txt", "r") as file:
        for line in file:
            print(line)


read_entire_file()


# 3. Append Text and Display
#
# Write a Python program to append text to a file and display the text.


def append_text_and_display(text: str):
    with open("files/data.txt", "a+") as file:
        file.write(text)

        for line in file:
            print(line)


append_text_and_display("writing...")


# 2. Bytes Concatenation
#
# Write a Python program that concatenates two given bytes objects.


def concat_bytes(byte1: bytes, byte2: bytes):
    return byte1 + byte2


def bytearray_from_list(list: list[int]):
    return bytearray(list)


def bytes_from_img():
    with open("files/data.txt", "rb") as img:
        bytes = img.read()

        with open("files/new.txt", "xb") as new:
            new.write(bytes)


# 1. OS Info and Directory Listing
#
# Write a Python program to get the name of the operating system (Platform independent), information of the current operating system,
# current working directory,
# print files and
# directories in the current directory, and raise errors if the path or file name is invalid.
import os
def os_info_and_directory_listing():
    
    print(os.name)
    print(os.uname_result)
    print(os.curdir)
    
    print(os.listdir(os.curdir))
    
os_info_and_directory_listing()    
    
path = 'g:\\testpath\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])    

def check_access(path):
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
    
import io    
def string_buffer(string: str):
       
    
    output = io.StringIO()
    output.write(string)
   
    print(output.getvalue())
    
    output.close()    
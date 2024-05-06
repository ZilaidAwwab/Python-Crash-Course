# Writing to a file

# One of the simplest ways to save data is to write it to a file. When you write text to a file, the output will still be available after you close the terminal containing your program’s output. You can examine output after a program finishes running, and you can share the output files with others as well. You can also write programs that read the text back into memory and work with it again later.

# Writing to an empty file
filename = "programming.txt"

with open(filename, "w") as file_object:
    file_object.write("I am a Python Developer\n")

    # Writing multiple lines

    # Incase of writing multiple lines we must add the new line character
    file_object.write("I am a Web developer\n")

# TIP:
#  Be careful opening a file in write mode ('w') because if the file does exist, Python will erase the file before returning the file object.

# This file behaves like any other file on your computer. You can open it, write new text in it, copy from it, paste to it, and so forth.

# Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.

# Here we have used "w" to write, although we have different options for different functions

# "r" for read
# "a" for append
# "r+" for reading and writing
# if we don't give any mode, then by default it opens the file in the read mode

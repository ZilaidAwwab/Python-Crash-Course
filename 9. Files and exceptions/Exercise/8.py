# Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.


def read_files(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print("The file contains following names:\n")
        print(contents)


read_files("cats.txt")
read_files("dogs.txt")

# this file don't exist
read_files("parrots.txt")

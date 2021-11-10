import errno

try:
    stream = open("filename", "r")
    print("File exists")
    stream.close()
except # complete the code
    # check if file does not exist
        print("The file doesn't exist")
    else:
        print("Something went wrong")

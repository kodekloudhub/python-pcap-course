import errno

try:
    stream = open("filename", "r")
    print("File exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("The file doesn't exist")
    else:
        print("Something went wrong")

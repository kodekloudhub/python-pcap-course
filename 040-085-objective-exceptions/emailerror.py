class EmailError(ValueError):
    # complete the class by adding status
    # and message arguments for the constructor


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError("pending!","wrong format!")
except EmailError as e:
    print(e)

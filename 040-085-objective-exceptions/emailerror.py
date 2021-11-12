class EmailError(ValueError):
    # complete the class by adding status
    # and message arguments for the constructor


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError("wrong format!", "pending!")
except EmailError as nve:
    print(e)

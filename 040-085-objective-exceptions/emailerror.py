class EmailError(ValueError):
    # complete the class by adding name
    # and status properties in the constructor


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError("wrong format", "pending")
except EmailError as nve:
    for arg in nve.args:
        print(arg, end='! ')

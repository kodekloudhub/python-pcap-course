class EmailError(ValueError):
    def __init__(self, name, status):
        self.data = (name, status)


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError("wrong format", "pending")
except EmailError as e:
    for arg in e.args:
        print(arg, end='! ')

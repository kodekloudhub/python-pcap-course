class EmailError(ValueError):
    def __init__(self, name="wrong format", status="pending"):
        self.data = (name, status)


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    for arg in e.args:
        print(arg, end='! ')

class EmailError(ValueError):
    def __init__(self, name="wrong format", status="pending"):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name + "! " + self.status + "!"


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    print(e)

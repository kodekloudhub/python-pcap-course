class EmailError(Exception):
    def __init__(self, status="pending!", message="wrong format!"):
        self.status = status
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.status + " " + self.message


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    print(e)

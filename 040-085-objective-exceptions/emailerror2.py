class EmailError(ValueError):
    # Add your code here

email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    print(e)

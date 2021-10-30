def err_fun(num):
    return 3 / num


try:
    err_fun(0)
except ZeroDivisionError:
    print("Cannot divide with zero!")

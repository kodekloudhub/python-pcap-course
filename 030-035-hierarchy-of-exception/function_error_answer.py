def err_fun(num):
    try:
        return 3 / num
    except ZeroDivisionError:
        print("Cannot divide with zero!")


err_fun(0)

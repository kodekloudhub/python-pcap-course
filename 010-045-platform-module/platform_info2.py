from platform import machine, system, python_version


def ask_user_info(spec):
    if spec == 'os':
        return system()
    elif spec == 'architecture':
        return machine()
    elif spec == 'python':
        return python_version()
    else:
        return "Sorry we couldn't answer your query"


print("Depending on your input we can show relevant info")
inp = input("Enter one of the words in [os, architecture, python]: ")
print(ask_user_info(inp))

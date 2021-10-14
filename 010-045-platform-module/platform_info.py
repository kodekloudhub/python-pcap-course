from platform import machine, system, python_version


def platform_info():
    user_os = system()
    user_arch = machine()
    user_python = python_version()
    return (user_os, user_arch, user_python)


print(platform_info())

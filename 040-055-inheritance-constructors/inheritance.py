class Super:
    # Add your code here
    supVar = 11


class Sub(Super):
    # Add your code here
    subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

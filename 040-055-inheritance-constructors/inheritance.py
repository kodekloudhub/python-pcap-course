class Super:
    # Add your code here
    supVar = 1


class Sub(Super):
    # Add your code here
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)

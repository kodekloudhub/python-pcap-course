class ObjCounter:
    # set the private 'counter' here

    def __init__(self, val=1):
        # set a private property 'first' to val

        # add here the counter


object_1 = ObjCounter()
object_2 = ObjCounter(2)
object_3 = ObjCounter(4)

print("Object_2 first: ", ...)
print("Object_3 first: ", ...)

print("We have created", end=" ")
print(object_3..., "objects")

print("Counter inside the ObjCounter is now", end=" ")
print(ObjCounter.__dict__["..."])

count = 0


def counter(the_list):
    global count
    for element in the_list:
        count += 1
    return len(the_list)


my_list = [i+1 for i in range(5)]
print(counter(my_list) == count)

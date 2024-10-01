import random as r


def gen_list():
    listy = []
    for x in range(10):
        listy.append(r.randint(-100, 100))
    return listy


def bubble(sorter):  # sorter is the list we are sorting
    while True:
        yummers = True
        for x in range(len(sorter) - 1):  # for the length of the list
            print(sorter)
            first = sorter[x]  # make a variable for the first number we are looking at
            next = sorter[(x + 1)]  # and second
            if first > next:  # and if the first number is large than the second,
                yummers = False  # make sure to flag we've changed something this loop,
                sorter[x + 1] = first  # then we flip the numbers in the list
                sorter[x] = next
        if yummers: break  # if this variable has not been changed in the loop, that means the sort is done.

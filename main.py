import random as r


def gen_list():
    listy = []
    for x in range(10):
        listy.append(r.randint(-100, 100))
    return listy


def bubble(sorter):  # sorter is the list we are sorting
    while True:
        yummers = True
        for x in range(len(sorter) - 1):
            print(sorter)
            first = sorter[x]
            next = sorter[(x + 1)]
            if first > next:
                yummers = False
                sorter[x + 1] = first
                sorter[x] = next
        if yummers: break
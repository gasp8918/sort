import random as r


def gen_list():
    listy = []
    for x in range(10):
        listy.append(r.randint(-100,100))
    return listy


def bubble(sorter): # sorter is the list we are sorting
    unsorted = False
    while unsorted:
        for x in len(sorter):
            first = sorter[x]
            next = sorter[(x+1)]
            if (first < next):
                

bubble(gen_list())
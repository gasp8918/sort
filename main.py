import random as r


def gen_list():
    listy = []
    for x in range(10):
        listy.append(r.randint(-100,100))
    return listy


def bubble(sorter):
    unsorted = False
    while unsorted:
        

bubble(gen_list())
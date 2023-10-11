from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(20)

print(seznam)

def bubble_sort(list_):
    for _ in range(len(seznam)):
        for poradi in range (len(seznam)-1):
            if seznam[poradi] > seznam[poradi+1]:
                seznam[poradi], seznam[poradi+1] = seznam[poradi+1],seznam[poradi]
    return seznam

print(bubble_sort(seznam))

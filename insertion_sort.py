from generator import get_random_list
from copy import deepcopy

seznam = get_random_list(20)

print(seznam)

def insertion_sort(list_):
    result=deepcopy(list_)
    i=1
    while i < len(result):
        p=i
        while p > 0:
            if result[p] < result[p-1]:
                result[p], result[p-1] = result[p-1], result[p]
            p-=1
        i+=1
    return result

print(insertion_sort(seznam))





















        
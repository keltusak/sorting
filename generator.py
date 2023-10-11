import random


def get_random_list(n, min=0, max=100):
    seznam=[]
    if min >= max:
        raise ValueError ("max must by greater then min")
    for _ in range(n):
        seznam.append(random.randint(min,max))
        #seznam += [random.randint(min,max)]
    #seznam=[random.randint(min,max) for _ in range(n)]
    
    return seznam

if __name__=="__main__":
    print(get_random_list(10))
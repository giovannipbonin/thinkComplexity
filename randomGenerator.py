import random
def linear_congruential_generator(seed):
    n = seed
    a = 22695477
    m = 2**32
    c = 1
    while (True):
        n = (a*n + c) % m
        yield n
   

i = 0
#gen = linear_congruential_generator(5)
while (i < 10**5):
#    print(next(gen))
    print(random.randint(0, 2**32))
    i += 1




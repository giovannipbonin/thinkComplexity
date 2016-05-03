def linear_congruential_generator(seed):
    n = seed
    a = 22695477
    m = 2**32
    c = 1
    while (True):
        n = (a*n + c) % m
        yield n
   


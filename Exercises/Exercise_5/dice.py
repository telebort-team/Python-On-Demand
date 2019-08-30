import random


def throw(num):
    total = 0
    for _ in range(num):
        total += random.randint(1, 6)
    return total

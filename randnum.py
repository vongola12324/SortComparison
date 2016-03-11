import random


def rand(upper):
    result = random.sample(list(range(1, upper * 2)), upper)
    random.shuffle(result)
    return result


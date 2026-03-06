import random


def random_integer():
    print("step into random_integer")
    return random.randint(0, 20)


def is_even_number():
    # 0 - 9
    num = random_integer()
    print("num is", num)
    if num % 2 == 0:
        return True
    # else:
    #     return False

    return False

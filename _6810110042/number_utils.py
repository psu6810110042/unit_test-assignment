def is_prime_list(numbers):
    for num in numbers:
        if num < 2:
            return False

        for n in range(2, num):
            if num % n == 0:
                return False

    return True

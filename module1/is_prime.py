def is_prime(n):
    div = 2
    if n == 1:
        return False
    while div <= n/2:
        if n % div == 0:
            return False
    return True


# print(is_prime(5))
# print(is_prime(4))
# print(is_prime(1))
# print(is_prime(6))
# print(is_prime(6546566668764))
# print(is_prime(668761))


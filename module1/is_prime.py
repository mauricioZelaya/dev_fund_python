def is_prime(n):
    div = 1
    counter = 0
    while div <= n/2:
        if n % div == 0:
            counter += 1
        div += 1
        if counter > 1:
            return False
    return True


print(is_prime(5))
print(is_prime(4))
print(is_prime(1))
print(is_prime(6))
print(is_prime(6546566668764))
print(is_prime(668761))


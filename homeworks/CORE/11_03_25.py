# 1
# def gen_primes():
#     already_primes = [2]
#     num = 2
#
#     while True:
#         is_prime = all(num % p != 0 for p in already_primes)
#
#         if is_prime:
#             already_primes.append(num)
#             yield num
#         num += 1
#
# prime_gen = gen_primes()
#
# print(next(prime_gen))
# print(next(prime_gen))
# print(next(prime_gen))
# print(next(prime_gen))

# 2
# import random
# def pass_gen(length):
#     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
#     already_pass = []
#     for _ in range(length):
#         yield random.choice(chars)
#
# password_1 = "".join(pass_gen(4))
# password_2 = "".join(pass_gen(4))
#
# print(f"Password 1: {password_1}\nPassword 2: {password_2}")
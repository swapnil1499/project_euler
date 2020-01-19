import time
import array as arr
import math
import numpy as np

start_time = time.time()

prime_n = 2000000  # Find primes till this number

primes = np.ones(prime_n, bool)
primes[0] = False  # 1 is not prime Number

for i in range(2, int(math.sqrt(prime_n)) + 1):
    if primes[i - 1]:
        isPrime = True
        x = 0
        while True:
            if (i ** 2 + i * x - 1) < prime_n:
                primes[i ** 2 + i * x - 1] = False
                x += 1
            else:
                break

sum_of_prime = 0
for i in range(0, len(primes)):
    if primes[i]:
        sum_of_prime = sum_of_prime + i + 1

print("answer = ", sum_of_prime)
print("--- %s seconds ---" % (time.time() - start_time))

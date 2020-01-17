import time
import array as arr
import math

start_time = time.time()

nth_prime = 10001  # nth prime that we are looking for
prime_list = arr.array('L', [2])

x = 3
while True:
    is_x_prime = True
    for i in prime_list:
        if x % i == 0:
            is_x_prime = False
            break
        if i > math.sqrt(x):
            break
    if is_x_prime:
        prime_list.append(x)

    if len(prime_list) == nth_prime:
        print("nth Prime = ", x)
        break
    x += 2

print("--- %s seconds ---" % (time.time() - start_time))

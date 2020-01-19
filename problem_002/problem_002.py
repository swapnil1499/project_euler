import time

start_time = time.time()


def evenFibonacciSum(limit):
    n_1 = 0  # first even seed
    n_2 = 2  # second even seed
    n = 0
    even_sum = n_1 + n_2
    while (n <= limit):
        n = 4 * n_2 + n_1
        n_1 = n_2
        n_2 = n
        if (n > limit):
            break
        even_sum += n
    return even_sum


print("ans is = %d" % evenFibonacciSum(4000000))
print("--- %s seconds ---" % (time.time() - start_time))

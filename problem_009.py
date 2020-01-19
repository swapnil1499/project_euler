import time

start_time = time.time()

for m in range(1, 32):
    for n in range(1, m):
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2
        if (a + b + c == 1000):
            print("answer = ", a * b * c)

print("--- %s seconds ---" % (time.time() - start_time))

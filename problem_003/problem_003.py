import time
import array as arr
import math

start_time = time.time()

number = 600851475143


def factors(n):
    x = 2
    y = 2
    cycle_size = 2
    d = 1

    while d == 1:
        count = 1
        while count <= cycle_size and d <= 1:
            x = (x ** 2 + 1) % n
            d = math.gcd(abs(x - y), n)
            count += 1
        cycle_size *=2
        y = x
    if d == n:
        return d
    else:
        return d


factorsList = arr.ArrayType('L', [1])

i = 0
while i != 1:
    temp = number
    for x in factorsList:
        temp = int(temp / x)
    i = factors(temp)
    #if i != temp:
    factorsList.append(i)

for x in factorsList:
    print(x)

print("--- %s seconds ---" % (time.time() - start_time))

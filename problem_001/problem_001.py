import time
start_time = time.time()

sum = 0
for x in range(1000):
    if (x % 3 == 0):
        sum = sum + x
    elif (x % 5 == 0):
        sum = sum + x

print("sum of all the multiples of 3 or 5 below 1000 is : %d" % sum)
print("--- %s seconds ---" % (time.time() - start_time))

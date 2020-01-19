import time

start_time = time.time()

sum_of_square = 0
square_of_sum = 0
for x in range(1, 101):
    sum_of_square += x**2
    square_of_sum += x

print("Answer = ", square_of_sum**2 - sum_of_square)

print("--- %s seconds ---" % (time.time() - start_time))

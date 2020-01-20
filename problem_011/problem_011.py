import time
import numpy as np

start_time = time.time()

f = open("number_grid.txt", 'r')
number_grid = f.read()
f.close()

number_list = number_grid.split()
n_grid = np.zeros([20, 20], int)

for i in range(0, 20):
    n_grid[i, :] = number_list[20 * i:(20 * i) + 20]

# for i in number_list:
product_h = 0
product_v = 0
product_d1 = 0
product_d2 = 0
product_ans = 0;
for m in range(0, 20):
    for n in range(0, 20):
        if n + 3 < 20:
            product_h = n_grid[m, n] * n_grid[m, n + 1] * n_grid[m, n + 2] * n_grid[m, n + 3]

        if m + 3 < 20:
            product_v = n_grid[m, n] * n_grid[m + 1, n] * n_grid[m + 2, n] * n_grid[m + 3, n]

        if n + 3 < 20 and m + 3 < 20:
            product_d1 = n_grid[m, n] * n_grid[m + 1, n + 1] * n_grid[m + 2, n + 2] * n_grid[m + 3, n + 3]

        if n - 3 >= 0 and m + 3 < 20:
            product_d2 = n_grid[m, n] * n_grid[m + 1, n - 1] * n_grid[m + 2, n - 2] * n_grid[m + 3, n - 3]

        if product_h > product_ans:
            product_ans = product_h

        if product_v > product_ans:
            product_ans = product_v

        if product_d1 > product_ans:
            product_ans = product_d1

        if product_d2 > product_ans:
            product_ans = product_d2

print("Answer = ", product_ans)
print("--- %s seconds ---" % (time.time() - start_time))

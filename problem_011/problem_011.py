import time

start_time = time.time()

f = open("number_grid.txt", 'r')
number_grid = f.read()

number_list = number_grid.split()

product_h = 1
product_v = 1
product_d = 1
for idx, x in enumerate(number_list):
    print(int(number_list[idx]))
    print(int(number_list[idx + 20]))
    if idx+3 >= 20:
        product_h = int(number_list[idx])*int(number_list[idx+1])*int(number_list[idx+2])*int(number_list[idx+3])
    product_v = int(number_list[idx])*int(number_list[idx+20])*int(number_list[idx+40])*int(number_list[idx+60])
    product_d = int(number_list[idx])*int(number_list[idx+21])*int(number_list[idx+42])*int(number_list[idx+63])

    if idx >= 0:
        break

print(product_h)
print(product_v)
print(product_d)
print("--- %s seconds ---" % (time.time() - start_time))

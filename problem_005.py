import time

start_time = time.time()

answer = 1
x = 20
while True:
    isAnswer = True
    for i in [3, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
        if x % i != 0:
            isAnswer = False
            break
    if isAnswer:
        print("answer = ", x)
        break
    x += 20

print("--- %s seconds ---" % (time.time() - start_time))

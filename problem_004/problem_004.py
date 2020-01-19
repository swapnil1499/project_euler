import time

start_time = time.time()
digits = 3

def isPalindrome(x):
    y = ''.join(reversed(x))
    if (x == y):
        return True
    else:
        return False


largest_palindrome = 0
for x in range(1, 10 ** digits):
    for y in range(1, 10 ** digits):
        product = x * y
        if (isPalindrome(str(product))) and product > largest_palindrome:
            largest_palindrome = product

print ("answer is = ", largest_palindrome)

print("--- %s seconds ---" % (time.time() - start_time))

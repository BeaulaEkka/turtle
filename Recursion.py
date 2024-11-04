def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

# factorials
# n!=nx(n-1)*(n-2)*...*1
# eg:3!=3*2*1


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(f'factorial:{factorial(4)}')
print(f'find sum:{find_sum(4)}')
# factorial(4)
# def factorial(4):
# if 4 == 0:
# return 1
# return 4 * factorial(4-1)

# This expands to:
# 4 * factorial(3)
# 4 * (3 * factorial(2))
# 4 * (3 * (2 * factorial(1)))
# 4 * (3 * (2 * (1 * factorial(0))))
# 4 * 3 * 2 * 1

print(f'factorial(5): {factorial(5)}')
# 5*4*3*2*1=120

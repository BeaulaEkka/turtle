# 1 1 2 3 5 8 13 21 ( by adding the previous two terms)
'''
(0+1)=1(takes initial sequence )
(1+1)=2
(2+1)=3
(3+2)=5
(5+3)=8
(8+5)=13
(13+8)=21
'''
# try out withouth recursion


def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        print(f'fib_sequence: {fib_sequence}')  # Print the updated sequence

    return fib_sequence  # Returns the entire sequence up to the nth term


# recursive


def fibonacci_recursive(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



print(f'Fibonacci-normal:{fibonacci(5)}')
print(f'fibonacci_recursive:{fibonacci_recursive(5)}')

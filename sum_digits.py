def sum_digits(n):
  if n < 0:
    print('Inputs must be greater than 0')
  result = 0
  while n != 0:
    result += n % 10
    n = n//10
    return result+n


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)
print(sum_digits(32))
print(sum_digits(-1))

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


a, b = int(input()), int(input())

division = factorial(a) / factorial(b)

print(f'{division:.2f}')

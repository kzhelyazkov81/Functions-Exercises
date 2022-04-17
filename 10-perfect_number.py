def perfect_check(number):
    divisors = []
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        message = 'We have a perfect number!'
    else:
        message = "It's not so perfect."
    print(message)


num = int(input())
perfect_check(num)

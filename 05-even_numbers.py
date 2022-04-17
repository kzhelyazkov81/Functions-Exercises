def odd_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)
        elif int(num) % 2 != 0:
            odd_sum += int(num)
    result = f'Odd sum = {odd_sum}, Even sum = {even_sum}'
    return result


num = input()
print(odd_even_sum(num))

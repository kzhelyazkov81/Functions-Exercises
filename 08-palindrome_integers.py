def palindrome_check(numbers):
    nums = numbers.split(', ')
    for num in nums:
        palindrome = True
        for i in range(len(num) // 2):
            if num[i] != num[-i-1]:
                palindrome = False
        print(palindrome)


palindrome_check(input())

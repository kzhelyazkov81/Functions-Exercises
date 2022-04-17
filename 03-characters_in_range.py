def characters(ch1, ch2):
    result = []
    for i in range(ord(ch1)+1, ord(ch2)):
        result.append(chr(i))
    characters_string = ' '.join(result)
    return characters_string


a, b = input(), input()

print(characters(a, b))

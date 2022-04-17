def length_check(password):
    valid = True
    if len(password) < 6 or len(password) > 10:
        valid = False
    return valid


def symbols_check(password):
    valid = True
    for i in password:
        if ord(i) < 48 or 57 < ord(i) < 65 or ord(i) > 122:
            valid = False
            break
    return valid


def digits_check(password):
    valid = True
    counter = 0
    for i in password:
        if 48 <= ord(i) <= 57:
            counter += 1
    if counter < 2:
        valid = False
    return valid


word = input()

if length_check(word) and symbols_check(word) and digits_check(word):
    print('Password is valid')
else:
    if not length_check(word):
        print('Password must be between 6 and 10 characters')
    if not symbols_check(word):
        print('Password must consist only of letters and digits')
    if not digits_check(word):
        print('Password must have at least 2 digits')

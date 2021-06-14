def if_vowels(char):
    vowels = "aouei"
    if char not in vowels:
        return True
    return False
print(''.join([el for el in input() if if_vowels(el)]))
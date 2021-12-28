def swap_case(s):
    new_word = ''
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            new_word += i.upper()
        else:
            new_word += i.lower()
    return new_word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
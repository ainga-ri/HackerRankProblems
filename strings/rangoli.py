# SLICING LISTS/STRINGS

def print_rangoli(size):
    # your code goes here
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    width = (n + n-1)
    word = ALPHABET[size-1]
    rangoli = ''
    for i in range(size,0, -1):
        lines = word.rjust(width, '-')
        # list[start:end:step]
        # https://www.youtube.com/watch?v=ajrtAuDg3yw
        rangoli = (rangoli + lines + lines[-2::-1] + '\n')
        word = word + '-' + ALPHABET[i-2]
    print(rangoli + rangoli[-size*4::-1])
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
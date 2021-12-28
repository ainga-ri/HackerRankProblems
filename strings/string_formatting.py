def print_formatted(number):
    # your code goes here
    max_space = len(str(bin(number)[2:])) + 1
    for i in range(1, number+1):
        space_length_decimal = ' ' * (max_space - len(str(i)) - 1)
        space_length_octal = ' ' * (max_space - len(str(oct(i)[2:])))
        space_length_hexadecimal = ' ' * (max_space - len(str(hex(i)[2:])))
        space_length_binary = ' ' * (max_space - len(str(bin(i)[2:])))

        print(space_length_decimal + '{}'.format(i) + 
            space_length_octal + '{}'.format(oct(i)[2:]) +
            space_length_hexadecimal + '{}'.format(hex(i)[2:]).upper() +
            space_length_binary + '{}'.format(bin(i)[2:]))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
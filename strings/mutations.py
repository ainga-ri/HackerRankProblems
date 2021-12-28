def mutate_string(string, position, character):
    mutation = list(string)
    mutation[position] = character
    return ''.join(mutation)
def slicing(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = slicing(s, int(i), c)
    print(s_new)
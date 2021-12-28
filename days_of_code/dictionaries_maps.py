n = int(input())
dictionary = {}
for i in range(n):
    key, value = input().split()
    dictionary[key] = value
print(dictionary)
while True: # we don't know how many names will be, we cannot put for j in range(n), because maybe it won't complete n names (quantity)
    try:
        name = input()
        if (name in dictionary):
            print(name + "=" + dictionary[name])
        else:
            print("Not found")
    except:
        break
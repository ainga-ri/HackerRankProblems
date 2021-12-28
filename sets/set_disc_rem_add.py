n = int(input())
s = set(map(int, input().split()))

N = int(input())
 
for i in range(N):
    instr = list(map(str, input().split()))
    if(instr[0] == 'pop'):
        s.pop()
    elif (instr[0] == 'remove'):
        s.remove(int(instr[1]))
    elif (instr[0] == 'discard'):
        s.discard(int(instr[1]))
        
print (sum(s))
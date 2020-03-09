n = int(input())
l = []
r = []
for i in range(n):
    s = input()
    c = s.split()
    if(c[0] == 'insert'):
        pos = int(c[1])
        val = int(c[2])
        l.insert(pos, val)
    elif(c[0] == 'print'):
        r.append(l[:])
    elif(c[0] == 'remove'):
        val = int(c[1])
        l.remove(val)
    elif(c[0] == 'append'):
        val = int(c[1])
        l.append(val)
    elif(c[0] == 'sort'):
        l.sort()
    elif(c[0] == 'pop'):
        l.pop()
    elif(c[0] == 'reverse'):
        l.reverse()
for i in r:
    print (i)


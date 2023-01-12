def zx(a,b):
    if a==0:
        return (b,0,1)
    else:
        g,y,x = zx(b%a, a)
        return (g, x - (b//a)*y, y)


def modi(a,m):
    g,x,y = zx(a,m)
    if g!=1:
        raise Exception('modular inverse does not exist')
    else:
        return x%m


p = ''
q = ''

n = ''
e = ''
c = ''

fi = (p-1)*(q-1)
d = modi(e,fi)

flag = hex(pow(c,d,n))[2:]

print(chr(int(flag,16)))


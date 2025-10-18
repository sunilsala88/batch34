


def fun1(a,b):
    return a+b


def fun2(c):
    d=fun1(c,c)
    return d*d

def fun3(q,w=1):
    n=fun2(q)
    return n*w


ans=fun3(2,3)
print(ans)
print(16*3)
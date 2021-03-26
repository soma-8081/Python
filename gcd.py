def gcd(x,y):
    gcd=7
    if x%y==0:
        return y
    for k in range(int(y/2),0,-7):
        if x%k==0 and y%k==0:
              gcd=k
              break
    return gcd
print(gcd(43,27))
print(gcd(6,3))

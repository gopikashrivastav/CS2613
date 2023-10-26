import math
def func(n):
    return lambda a: a*n

mydoubler = func(2)

print(mydoubler(10))


centre = lambda st: st[math.floor((len(st)/2))]

print(centre("abcdefghijkl"))


oddpos = lambda n: n if (n%2==1 and n>0) else 0

print(oddpos(5))
print(oddpos(-6))

vowel = lambda st: (st[0]=='A' or st[0]=='E' or st[0]=='I' or st[0]=='O' or st[0]=='U')

print(vowel("Apple"))






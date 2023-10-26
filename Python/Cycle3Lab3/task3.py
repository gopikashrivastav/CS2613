import math

#1
def func(n):
    return lambda a: a*n

mydoubler = func(2)

list1 = [8,10,7.5]
result = map(mydoubler, list1 )

print(list(result))

#2
list2 = ["Hello!", "CompSci2613", "Lab-12"]
centre = lambda st: st[math.floor((len(st)/2))]
result2= map(centre, list2)

print(list(result2))

#3
print("q3")
newlist = []
list3 = [-15, -4, 0, 4, 23, 64, 101, 123]
oddpos = lambda n: n if (n%2==1 and n>0) else 0
result3 = map(oddpos, list3)
for i in result3:
    if(i!=0):
        newlist = newlist + [i]

print(newlist)

#4
print("q4")
newlist2 = []
list4 = ["alice", "bob", "Carl", "daisy", "Earl"]
vowel = lambda st: (st[0]=='A' or st[0]=='E' or st[0]=='I' or st[0]=='O' or st[0]=='U')
result4 = list(map(vowel, list4))
# print(list(result4))
for i in range(0, len(list4)):
    if(result4[i]):
        newlist2.append(list4[i])
print(newlist2)
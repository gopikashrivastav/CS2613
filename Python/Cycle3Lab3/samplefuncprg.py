# x = lambda a,b: a * b
# print(x(5,20))

def myfunc(n):
    return lambda a: a *n


#creates a function that always doubles the value passed in
mydoubler = myfunc(2)

#creates a function that always doubles the value passed in
mytens = myfunc(10)

print(mydoubler(13))
print(mytens(3))


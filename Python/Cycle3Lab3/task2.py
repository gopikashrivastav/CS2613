# def func(a,b):
#     return lambda st: a>b

# #greaterthan = func(2,4)

# print(func(2,4))


# greaterthan = lambda a,b: (a>b)
# isgreater = a if(greaterthan(a,b)) elif()
# print(isgreater)


isgreater = lambda a,b: a if(a>b) else b
print(isgreater(5,6))
print(isgreater(7,3))


import math

def calc(a,b):

    result = math.sqrt(absolute(((a-1)**5) - absolute(b+1)))
    return result


def absolute(x):
    if x < 0:
        return -x
    else:
        return x


print("Input two values")
a = (input())
b = (input())
if(a!="X"):
    a = float(a)
    b = float(b)
print(calc(a,b))

while(a!= 'X'):
    print("Input two values")
    a = (input())
    b = (input())
    print(calc(a,b))
    if(a=="X"):
        print("error")


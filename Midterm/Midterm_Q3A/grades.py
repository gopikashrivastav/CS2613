f = open("ExampleInput.txt", "r+")
data = f.read()
#file is opened and read into data
dataArr= data.split() 
#data stored in a list
#print(stArr)

sum = 0
count = 0
ca = 0
cb = 0
cc = 0
cd = 0
cf = 0
#converting data to float

for st in dataArr:
    st = float(st)

    if(st<0 or st>100):
        continue
    else:
        count = count+1
        sum = sum+st
        if(st>=80 and st<=100):
            print("A")
            ca = ca+1
        elif(st>=65 and st<=79.99):
            print("B")
            cb = cb+1
        elif(st>=55 and st<=64.99):
            print("C")
            cc = cc+1
        elif(st>=50 and st<=54.99):
            print("D")
            cd = cd+1
        elif(st>=0 and st<=49.99):
            print("F")
            cf = cf+1

#print(type(stArr))

average = sum/count
print("Average grade is: ", average)

avgcount = 0
#finding number of grades above average grade
for st in dataArr:
    st = float(st)
    if(st>average):
        avgcount = avgcount+1

print("A", ca)
print("B", cb)
print("C", cc)
print("D", cc)
print("F", cf)
print("The number of grades above the average grade is: ", avgcount)
f.close()
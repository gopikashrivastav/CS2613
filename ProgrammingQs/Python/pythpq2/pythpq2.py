f = open("DataInput.txt", "r")
sum = 0
data = f.read()
clean_data=data.replace('\n', ' ')


s = 0
#count = 0
data = clean_data.split()
#print(type(data), data)
for i in range(0, len(data)):
    if(data[i]=="SUM"):
        i=i+1
        while(data[i]!='AVG'):
            sum = sum + float(data[i])
            i=i+1
    # elif(data[i]=="AVG"):
    #     i=i+1
    #     while(data[i]!='MAX'):
    #         s = s + float(data[i])
    #         count = count + 1
        

print("Sum:" ,sum)
#print("Average:" , s/count)



# print(data)


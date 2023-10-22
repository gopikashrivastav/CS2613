name = input("Hello, please input a name! ")
age = int(input("Please input the age! "))

while(age<0 or age>122):
    print("Error in input, try again")
    age = int(input("Please input the age! "))

    

if age>=0 and age<=15:
    print(name , "must wait", 16-age, "years to get a driver's license!")

elif age == 16:
    print("Congrats!", name, "can get their driver's license now!")

elif age >=17 and age <=122:
    print(name, "has been eligible for a driver's license for", age-16, "years!")

#print("Name" , name)
#print("Age", age, end = "")


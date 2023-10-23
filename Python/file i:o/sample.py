# Open a file
#also creates foo.txt
f = open("foo.txt", "r+")
print("Name of the file: ", f.name)
print("Closed or not : ", f.closed)
print("Opening mode : ", f.mode)

#Writing
f.write("hiiii!")

#Reading
#read() function takes as a paramter the number of bytes to be read.
str = f.read(1)
print(str)

#Checking position 
pos = f.tell()
print("current file position is", pos)

#changing position
pos = f.seek(0,0) #pointer at beginning again
st = f.read()
print("Again read string is: ", st)
# Close opened file
f.close()
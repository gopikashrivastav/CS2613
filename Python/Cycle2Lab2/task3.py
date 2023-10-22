fin = open('L6_T4_Text.txt')
#lines = fin.readlines()

#list1 = lines.split()
#print(lines)
#print(type(lines))

for line in fin:
    count = 0
    word = line.strip()
    #print(word)
    if(len(word)==5):
       print(word)
#print("words that are 5 letter words:", count)


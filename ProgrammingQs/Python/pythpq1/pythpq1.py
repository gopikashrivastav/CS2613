import re 

def clean_token(st):
   st = st.lower()
   print("The string in lower case is:" , st)
   st = re.sub(r'[^a-zA-Z0-9\s]+', '', st)
   #st = ''.join(filter(str.isalnum, st))
   print("String with nonalphanumeric characters removed: ", st)

def repeat_letter(st):
    check = False
    for i in range(0,len(st)):
        for j in range(i+1, len(st)):
            if(st[j]==st[i]):
                check = True
    
    return check

def end_start_char(st1, st2):
    if(st1[-1]==st2[0]):
        return True
    else:
        return False

def report():
    st = input("Input a string")
    clean_token(st)
    stArr=st.split()
    countRc = 0
    countES = 0
    for idx, i in enumerate(stArr):
        if(repeat_letter(i)):
            countRc = countRc +1
        for j in range(idx+1 ,len(stArr)):
            if(end_start_char(i,stArr[j])):
                countES = countES + 1

    countAl = len(re.findall('[a-zA-Z]', st))
    
    print("Total number of number of alphabetic characters: " , countAl)
    print("Total number of words with a repeated character: " , countRc)
    print("Total number of number of end-start matches: " , countES)
    

report()





    


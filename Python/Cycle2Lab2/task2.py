def given_length(st, a):
    list1 = st.split()
    print(list1)

    for i in list1:
        l = len(i)
        if(l!=a):
            list1.remove(i)
    print(list1)


def longest_word(st):
    list2 = st.split()
    print(list2)

    maxl = 0
    listnew = []

    for i in list2:
        l = len(i)
        if(l>maxl):
            maxl = l
            listnew = [i]
    print(listnew)

def most_common(st3):
    maxCount = 0
    count = 0
    listnew = []
    list3 = list(st3)
    #print(list3)
    i=0
    j=1
    for i in list3:
        
        for j in list3:
            if(j==i):
                count = count+1
                if(count>maxCount):
                    maxCount = count
                    st = j
    print(st)

        











given_length("The white cat and the red fox.", 3)

longest_word("Hello CS2613! Python is fun.")

most_common("My name is Gopika")




mystring = "aabccbcadbbbaaf"
repdic = {}
for ch in mystring: 
    try:
        repdic[ch.lower()]+=1
    except:
        repdic[ch.lower()]=1
for ch in mystring: 
    if repdic[ch.lower()]==1: 
        print(ch) 
        exit()

# Reverse Vowels In A String
text = "applePIe"
v_list = ["A","E","I","O","U"]
ltext = list(text)
ltext_len = len(ltext)
i = 0
j = ltext_len-1
#print(f"origin:{str(ltext)}")
    
while(not i>=j):
    while not (ltext[i].upper() in v_list): i+=1
    while not (ltext[j].upper() in v_list): j-=1   
    if (i>=j):  exit()   
    lv = ltext[i]
    ltext[i] = ltext[j]
    ltext[j] = lv
    #print(f"i={str(i)},j={str(j)},{str(ltext)}")
    i+=1
    j-=1

print("'"+text+"' is converted to '"+''.join(ltext)+"'")    

        

        

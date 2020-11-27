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

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         repdic = {}
#         for ch in s: 
#             try:
#                 repdic[ch.lower()]+=1
#             except:
#                 repdic[ch.lower()]=1
#         for chi in range(len(s)): 
#             if repdic[s[chi].lower()]==1: 
#                 return(chi)      
#         return(-1)

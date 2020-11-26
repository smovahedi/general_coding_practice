# Description
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally 
# (horizontal or vertical). You may assume all four edges of the grid are surrounded by water.

# Count the number of distinct islands. An island is considered to be the same as another if and only if one island has the same shape 
# as another island (and not rotated or reflected).

# Example 1:

# Input: 
#   [
#     [1,1,0,0,1],
#     [1,0,0,0,0],
#     [1,1,0,0,1],
#     [0,1,0,1,1]
#   ]
# Output: 3


# Example 2:

# Input:
#   [
#     [1,1,0,0,0],
#     [1,1,0,0,0],
#     [0,0,0,1,1],
#     [0,0,0,1,1]
#   ]
# Output: 1 
    
import numpy as np 
user_input = np.array([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]])
print(user_input)

def splitmat(data):
    lastdata = []

    for colar in data:
        colsum = colar.sum(axis=0)
        #print(colsum)
        col_splited_data = np.hsplit(colar,np.where(colsum==0)[0])
        #print(col_splited_data)

        for ar in col_splited_data:
            ar_noZeroCol = ar[:,~np.all(ar == 0, axis = 0)]
            if (ar_noZeroCol.size == 0): continue
            #print(ar)
            #print(ar_noZeroCol)
            rowsum = ar_noZeroCol.sum(axis=1)
            for subar in np.vsplit(ar_noZeroCol,np.where(rowsum==0)[0]):
                #print(f"subar: {subar}")
                ri = np.all(subar == 0, axis = 1)
                #print(ri)
                subar_noZeroRow = subar[~ri,:]
                exist = False
                for i in lastdata: 
                    if np.array_equal(subar_noZeroRow,i): exist = True
                if not (subar_noZeroRow.size == 0) and not exist : lastdata.append(subar_noZeroRow)
                
        
    return(lastdata)

indata = [user_input]
datasplit = splitmat(indata)
comp = indata == datasplit
print(indata)
print(datasplit)
print(comp)

while (not comp):  
    indata = datasplit
    datasplit = splitmat(indata)
    print(indata)
    print(datasplit)
    flag = 0
    for i in indata:
        for j in datasplit:
            if np.array_equal(i,j):
                flag += 1
    comp = len(indata) == len(datasplit) and flag==len(datasplit)
    print(comp)

print(f"\n** There are {str(len(datasplit))} unique islands! **")
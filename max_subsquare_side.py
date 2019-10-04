mat = [[0,0,0,0,1],
       [1,0,1,1,1],
       [1,0,1,0,1],
       [1,1,1,1,1],
       [0,0,1,1,1]]
       
def tag_mat(mat,ridx,cidx):

    if ridx == 0 and cidx == 0:
        if mat[ridx][cidx] == 1:
            return (1,1)
        else:
            return (0,0)

    if mat[ridx][cidx] == 1:
        if ridx ==0:
            c1 = 1
        else:
            c1 = tag_mat(mat,ridx-1,cidx)[0]+1
            
        if cidx ==0:
            c2 =1
        else:
            c2 = tag_mat(mat,ridx,cidx-1)[1]+1
        return (c1,c2)
    else:
        return (0,0)
        
def find_mss(tmat, ridx, cidx):
    print(ridx,cidx)
    if ridx < 0 or cidx < 0:
        return 0
    
    if tmat[ridx][cidx][0] ==0:
        return 0

    if ridx == 0 or cidx == 0: 
        return 1 
        
    for ed in range(0, min(tmat[ridx][cidx][0], tmat[ridx][cidx][1])):
        if tmat[ridx][cidx-ed][0] >= ed and tmat[ridx-ed][cidx][1] >= ed:
            print('a',ridx,cidx,ed)
        else:
            return ed
    return ed 
    
tmat = []
for i in range(0, len(mat)):
    row = []
    for j in range(0, len(mat[0])):
        row.append(tag_mat(mat, i, j))
    tmat.append(row)

mss = []
for i in range(0, len(mat)):
    for j in range(0, len(mat[0])):
        mss.append(find_mss(tmat, i, j))

print(mss)    

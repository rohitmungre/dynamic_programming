mat = [[2,3], [3,6], [6,4], [4,5]]

def min_cost_dp(mat, sidx, eidx, memo):
    
    mstr = str(sidx)+'~'+str(eidx)
    if mstr in memo:
        return memo[mstr]

    if sidx >= eidx: 
        memo[mstr] = 0
        return 0
    
    if sidx == eidx -1: 
        memo[mstr] = mat[sidx][0] * mat[sidx][1] * mat[eidx][1]
        return mat[sidx][0] * mat[sidx][1] * mat[eidx][1]
        
    c_arr = []
    for i in range(sidx, eidx):
        c_arr.append(min_cost_dp(mat, sidx, i, memo) + min_cost_dp(mat,i+1,eidx, memo) + mat[sidx][0]*mat[i][1]*mat[eidx][1])

    min_carr = min(c_arr)
    memo[mstr] = min_carr
    
    return min_carr
    

def min_cost(mat, sidx, eidx):
    
    if sidx >= eidx: 
        return 0
    
    if sidx == eidx -1: 
        return mat[sidx][0] * mat[sidx][1] * mat[eidx][1]
        
    c_arr = []
    for i in range(sidx, eidx):
        c_arr.append(min_cost(mat, sidx, i) + min_cost(mat,i+1,eidx) + mat[sidx][0]*mat[i][1]*mat[eidx][1])

    min_carr = min(c_arr)
    
    return min_carr
    
print(min_cost(mat,0,3))
print(min_cost_dp(mat,0,3, {}))

mat = (5,5)

def find_ways_dp(mat, sidx, eidx, memo):
    mstr = str(sidx)+'~'+str(eidx)
    if mstr in memo:
        return memo[mstr]
    
    if sidx == mat[0]-1 and eidx == mat[1]-1: 
        memo[mstr] = 1
        return 1
        
    if sidx == mat[0]-1:
        memo[mstr] = find_ways_dp(mat,sidx,eidx+1, memo)
        return find_ways_dp(mat,sidx,eidx+1,memo)
        
    if eidx == mat[1]-1:
        memo[mstr] = find_ways_dp(mat,sidx+1,eidx,memo)
        return find_ways_dp(mat,sidx+1,eidx, memo)
    
    c1 = find_ways_dp(mat, sidx,eidx+1,memo)
    c2 = find_ways_dp(mat, sidx+1,eidx,memo)
    
    memo[mstr] = c1+c2
    return c1+c2
    
def find_ways(mat, sidx, eidx):
    if sidx == mat[0]-1 and eidx == mat[1]-1: 
        return 1
        
    if sidx == mat[0]-1:
        return find_ways(mat,sidx,eidx+1)
        
    if eidx == mat[1]-1:
        return find_ways(mat,sidx+1,eidx)
    
    c1 = find_ways(mat, sidx,eidx+1)
    c2 = find_ways(mat, sidx+1,eidx)
    
    return c1+c2

print(find_ways(mat, 0, 0))
print(find_ways_dp(mat, 0, 0, {}))

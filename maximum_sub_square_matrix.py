mat = [ [0,0,1,1,1],
        [1,1,1,1,1],
        [0,0,1,1,1],
        [1,0,1,1,1]]

def max_sub_sqr(mat, ridx, cidx): 
    
    if ridx >= len(mat) or cidx >= len(mat[0]) or ridx < 0 or cidx < 0:
        return 0
    
    if mat[ridx][cidx] == 0: 
        return 0 
    
    c1 = max_sub_sqr(mat, ridx -1, cidx)
    c2 = max_sub_sqr(mat, ridx -1, cidx -1)
    c3 = max_sub_sqr(mat, ridx, cidx -1)

    return min(c1, c2, c3)+1    

def max_sub_sqr_dp(mat, ridx, cidx, memo): 
    
    mstr = str(ridx) + '~' + str(cidx)
    if mstr in memo:
        return memo[mstr]
    
    if ridx >= len(mat) or cidx >= len(mat[0]) or ridx < 0 or cidx < 0:
        memo[mstr] = 0
        return 0
    
    if mat[ridx][cidx] == 0: 
        memo[mstr] = 0
        return 0 
    
    c1 = max_sub_sqr(mat, ridx -1, cidx)
    c2 = max_sub_sqr(mat, ridx -1, cidx -1)
    c3 = max_sub_sqr(mat, ridx, cidx -1)

    memo[mstr] = min(c1,c2,c3)+1
    return min(c1, c2, c3)+1    

def mss_wrapper(mat):
    ss_arr = []
    memo = {}
    for cidx in range(0,len(mat[0])):
        for ridx in range(0, len(mat)):
            ss_arr.append(max_sub_sqr_dp(mat, ridx, cidx, memo))
            
    return max(ss_arr)
    
print(mss_wrapper(mat))

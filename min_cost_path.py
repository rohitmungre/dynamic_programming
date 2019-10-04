mat = [[1,3,5,8],
       [4,2,1,7],
       [4,3,2,3]]

def min_cost_path_dp(mat, ridx, cidx, memo):
    mstr = str(ridx)+ '~' + str(cidx)
    if mstr in memo:
        return memo[mstr]
    
    if ridx == len(mat) - 1 and cidx == len(mat[0]) -1:
        memo[mstr] = mat[ridx][cidx]
        return memo[mstr]
        
    if ridx == len(mat) -1:
        memo[mstr] = mat[ridx][cidx]+ min_cost_path_dp(mat,ridx, cidx+1, memo)
        return memo[mstr]
        
    if cidx == len(mat[0]) - 1:
        memo[mstr] = mat[ridx][cidx] + min_cost_path_dp(mat,ridx+1,cidx, memo)
        return memo[mstr]
        
    c1 = min_cost_path_dp(mat, ridx, cidx+1, memo)
    c2 = min_cost_path_dp(mat, ridx+1, cidx, memo)

    memo[mstr] = mat[ridx][cidx] + min(c1,c2)
    return memo[mstr]
       
def min_cost_path(mat, ridx, cidx):
    if ridx == len(mat) - 1 and cidx == len(mat[0]) -1:
        return mat[ridx][cidx]
        
    if ridx == len(mat) -1:
        return mat[ridx][cidx]+ min_cost_path(mat,ridx, cidx+1)
        
    if cidx == len(mat[0]) - 1:
        return mat[ridx][cidx] + min_cost_path(mat,ridx+1,cidx)
        
    c1 = min_cost_path(mat, ridx, cidx+1)
    c2 = min_cost_path(mat, ridx+1, cidx)
    
    return mat[ridx][cidx] + min(c1,c2)
    
print(min_cost_path(mat, 0, 0))
print(min_cost_path_dp(mat, 0, 0, {}))

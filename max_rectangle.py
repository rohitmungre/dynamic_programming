mat = [[1,0,0,1,1,1],
       [1,0,1,1,0,1], 
       [0,1,1,1,1,1],
       [0,0,1,1,1,1]]

def max_sub_rectangle_dp(mat, ridx, cidx, memo):
    mstr = str(ridx)+'~'+str(cidx)
    if mstr in memo:
        return memo[mstr]
    
    if ridx < 0 or cidx < 0: 
        memo[mstr] = (0,0)
        return memo[mstr]
    
    if mat[ridx][cidx] == 0:
        memo[mstr] = (0,0)
        return memo[mstr]

    if mat[ridx-1][cidx] == 0:
        (left_val1, left_val2) = max_sub_rectangle_dp(mat, ridx,cidx-1, memo)
        memo[mstr] = (1, left_val2+1)
        return memo[mstr]

    if mat[ridx][cidx-1] == 0:
        (up_val1, up_val2) = max_sub_rectangle_dp(mat, ridx-1,cidx, memo)
        memo[mstr] = (up_val1+1, 1)
        return memo[mstr]

    if mat[ridx-1][cidx-1] == 0:
        (left_val1, left_val2) = max_sub_rectangle_dp(mat, ridx,cidx-1, memo)
        (up_val1, up_val2) = max_sub_rectangle_dp(mat, ridx-1,cidx, memo)
        
        if left_val2 > up_val1:
            memo[mstr] = (1, left_val2+1)
            return memo[mstr]
        else:
            memo[mstr] = (up_val1+1, 1)
            return memo[mstr]

    (left_val1, left_val2) = max_sub_rectangle_dp(mat, ridx,cidx-1, memo)
    (up_val1, up_val2) = max_sub_rectangle_dp(mat, ridx-1,cidx, memo)
    (diag_val1, diag_val2) = max_sub_rectangle_dp(mat, ridx-1, cidx-1, memo)
    
    val1 = min(up_val1, diag_val1) + 1
    val2 = min(left_val2, diag_val2) + 1
    
    memo[mstr] = (val1, val2)
    return memo[mstr]

       
def max_sub_rectangle(mat, ridx, cidx):
    if ridx < 0 or cidx < 0: 
        return (0,0)
    
    if mat[ridx][cidx] == 0:
        return (0,0)
        
    if mat[ridx-1][cidx] == 0:
        (left_val1, left_val2) = max_sub_rectangle(mat, ridx,cidx-1)
        return (1, left_val2+1)

    if mat[ridx][cidx-1] == 0:
        (up_val1, up_val2) = max_sub_rectangle(mat, ridx-1,cidx)
        return (up_val1+1, 1)

    if mat[ridx-1][cidx-1] == 0:
        (left_val1, left_val2) = max_sub_rectangle(mat, ridx,cidx-1)
        (up_val1, up_val2) = max_sub_rectangle(mat, ridx-1,cidx)
        
        if left_val2 > up_val1:
            return (1, left_val2+1)
        else:
            return (up_val1+1, 1)
        
    (left_val1, left_val2) = max_sub_rectangle(mat, ridx,cidx-1)
    (up_val1, up_val2) = max_sub_rectangle(mat, ridx-1,cidx)
    (diag_val1, diag_val2) = max_sub_rectangle(mat, ridx-1, cidx-1)
    
    val1 = min(up_val1, diag_val1) + 1
    val2 = min(left_val2, diag_val2) + 1
    
    return (val1, val2)
    
print(max_sub_rectangle(mat, 3,5))
print(max_sub_rectangle_dp(mat, 3,5, {}))

max_area = 0
memo ={}
for i in range(0,len(mat)):
  for j in range(0,len(mat[0])):
    (val1, val2) = max_sub_rectangle_dp(mat, i, j , memo)
    prod = val1*val2
    if prod > max_area:
      max_area = prod

print(prod)

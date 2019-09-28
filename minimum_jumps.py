arr = [2,3,1,1,2,4,2,0,1,1]

arr = [1,2,3,4,5,1,1,1,1]
def min_jumps_dp(arr, idx, memo):
    
    if idx in memo:
        return memo[idx]
        
    if idx >= len(arr):
        memo[idx] = 0
        return 0
      
    j1=0
    if arr[idx]!=0:  
        j1 = 1+min_jumps_dp(arr, idx+arr[idx], memo)
    j2 = 1+min_jumps_dp(arr, idx+1, memo)
    
    memo[idx] = min(j1,j2)
    return min(j1, j2)


def min_jumps(arr, idx):
    
    if idx >= len(arr):
        return 0
      
    j1=0
    if arr[idx]!=0:  
        j1 = 1+min_jumps(arr, idx+arr[idx])
    j2 = 1+min_jumps(arr, idx+1)
    
    return min(j1, j2)
    
print(min_jumps(arr,0))
print(min_jumps_dp(arr,0,{}))

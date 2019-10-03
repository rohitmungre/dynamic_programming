arr = [3,4,-1,0,6,2,3,-1,-1]

def lis_wrapper(arr, idx):
    len_arr = []
    memo = {}
    for i in range(0,idx+1):
        len_arr.append(longest_increasing_subsequence_dp(arr, i, memo))
    print(len_arr)
    return max(len_arr)    

def longest_increasing_subsequence_dp(arr, idx, memo):
    
    if idx in memo:
        return memo[idx]

    tidx = idx -1 
    while arr[tidx]>arr[idx] and tidx>=0:
        tidx = tidx -1
    
    if tidx < 0:
        memo[idx] = 1
        return 1 
    
    memo[idx] = longest_increasing_subsequence_dp(arr, tidx, memo)+1 
    return longest_increasing_subsequence_dp(arr, tidx, memo)+1 


def longest_increasing_subsequence(arr, idx):
    
    tidx = idx -1 
    while arr[tidx]>arr[idx] and tidx>=0:
        tidx = tidx -1
    
    if tidx < 0:
        return 1 
    
    return longest_increasing_subsequence(arr, tidx)+1 
    
print(lis_wrapper(arr,8))

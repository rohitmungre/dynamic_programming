arr = [4,1,1,4,2,1,0]

def max_na_ss_dp(arr,idx,memo):
    
    if idx in memo:
        return memo[idx]

    if idx == 0 or idx == 1:
        memo[idx] = arr[idx]
        return arr[idx]
        
    i = idx-2
    mss = 0 
    while i >= 0:
        tmp = max_na_ss(arr,i)
        if tmp > mss:
            mss = tmp
        i = i-1
    
    memo[idx] = mss + arr[idx]        
    return mss + arr[idx]


def max_na_ss(arr,idx):
    
    if idx == 0 or idx == 1:
        return arr[idx]
        
    i = idx-2
    mss = 0 
    while i >= 0:
        tmp = max_na_ss(arr,i)
        if tmp > mss:
            mss = tmp
        i = i-1
        
    return mss + arr[idx]

def mnass_wrapper(arr, idx):
    res = 0
    memo = {}
    for i in range(0,idx+1):
        tmp = max_na_ss_dp(arr, i, memo)
        print(i,tmp)
        if tmp > res:
            res = tmp
    return res
    
print(mnass_wrapper(arr,6))        

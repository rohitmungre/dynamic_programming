import copy

prices = [2,5,7,1,4,3,1,3,1,19]
k =4

def max_profit_dp(prices, k, idx, memo):
    
    if k == 0: 
        return 0

    if len(prices) == 0: 
        return 0
        
    if idx <= 0:
        return 0

    mstr = str(idx)+'~'+str(k)
    if mstr in memo: 
        return memo[mstr]
        
    cp = prices[idx]
    
    s1 = max_profit_dp( prices, k, idx-1, memo)
    s2 = 0
    for m in range(0, idx):
        if prices[m]<=prices[idx]:
            tmp = prices[idx] - prices[m] + max_profit_dp(prices, k-1, m-1, memo)
            if s2 < tmp: 
                s2 = tmp
    
    memo[mstr] = max(s1,s2)
    return max(s1, s2)



def max_profit(prices, k, idx):
    
    if k == 0: 
        return 0
        
    if len(prices) == 0: 
        return 0
        
    if idx <= 0:
        return 0
        
    cp = prices[idx]
    
    s1 = max_profit( prices, k, idx-1)
    s2 = 0
    for m in range(0, idx):
        if prices[m]<=prices[idx]:
            tmp = prices[idx] - prices[m] + max_profit(prices, k-1, m-1)
            if s2 < tmp: 
                s2 = tmp
            
    return max(s1, s2)
    
print(max_profit(prices, k , 9))
print(max_profit_dp(prices, k , 9, {}))

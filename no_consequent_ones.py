n = 2

def no_cons_ones_dp(n, memo):
    if n in memo:
        return memo[n]
    
    if n <1: 
        memo[n]=0
        return 0
    if n == 1: 
        memo[n]=2
        return 2
    if n == 2 : 
        memo[n]=3
        return 3
    memo[n] = no_cons_ones_dp(n-1,memo) + no_cons_ones_dp(n-2,memo)
    return no_cons_ones_dp(n-1,memo) + no_cons_ones_dp(n-2, memo)


def no_cons_ones(n):
    if n <1: 
        return 0
    if n == 1: 
        return 2
    if n == 2 : 
        return 3
    return no_cons_ones(n-1) + no_cons_ones(n-2)
    
print(no_cons_ones(5))
print(no_cons_ones_dp(5, {}))

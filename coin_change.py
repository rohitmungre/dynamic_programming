import copy

def find_min_coins(coin_set, sum):
    
    if sum == 0: 
        return 0 
        
    if (len(coin_set)<1) or (sum<0):
        return -100000
    
    el = coin_set.pop()
    count = 0 
    res_set = []
    
    while sum>-1:
        coin_set_copy = copy.copy(coin_set)
        res_set.append(count + find_min_coins(coin_set_copy , sum))
        sum = sum - el
        count = count + 1

    res = min(i for i in res_set if i > 0)
    return res

coin_set = [1, 10, 25]
sum = 32

print(find_min_coins(coin_set, sum))
print('abcdefabc'.split('abc',1))

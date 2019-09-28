import math

floors = 10 
eggs = 2

def find_attempt_dp(floors, eggs, memo):
    
    mstr = str(floors) + '~' + str(eggs)
    if mstr in memo:
        return memo[mstr]
    
    if eggs <= 0:
        memo[mstr] = 0
        return 0
    
    if eggs == 1: 
        memo[mstr] = floors
        return floors
        
    attempts = 0
    while eggs > 1: 
        floors = math.ceil(floors/2)
        eggs = eggs -1
        print(floors,eggs)
        attempts = 1 + find_attempt_dp(floors,eggs, memo)
        
    memo[mstr] = attempts
    return attempts


def find_attempt(floors, eggs):
    
    if eggs <= 0:
        return 0
    
    if eggs == 1: 
        print(floors,eggs)
        return floors
        
    attempts = 0
    while eggs > 1: 
        floors = math.ceil(floors/2)
        eggs = eggs -1
        print(floors,eggs)
        attempts = 1 + find_attempt(floors,eggs)
        
    return attempts
    
print(find_attempt_dp(floors, eggs, {}))

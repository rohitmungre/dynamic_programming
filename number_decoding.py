def num_ways_dp(st, di, memo):
    if st in memo:
        return memo[st]
    
    if len(st) == 0: 
        return 1
    
    ways = 0
    for item in di: 
        if st.startswith(item):
            temp, nst = st.split(item,1)
            ways = ways + num_ways_dp(nst, di, memo)
    
    memo[st] = ways
    return ways
    
def num_ways(st, di):
    if len(st) == 0:
        return 1
    
    ways = 0
    for item in di: 
        if st.startswith(item):
            temp, nst = st.split(item,1)
            ways = ways + num_ways(nst, di)
    
    return ways 


dic = {'a':'1' , 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h': '8', 'i': '9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21','v': '22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
di = {'1':'a','2':'b', '3':'c', '13':'m', '14':'n'}
st = '13'

print(num_ways_dp(st, di,{}))

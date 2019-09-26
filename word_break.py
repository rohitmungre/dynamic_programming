def word_break_dp(st, di, memo):
    
    if st in memo: 
        return memo[st]
        
    if len(st) == 0: 
        print('Yay')
        return 1
    
    path = 0
    for item in di: 
        if st.startswith(item):
            print(st)
            print(item)
            temp, nst = st.split(item,1)
            path = path + word_break_dp(nst, di, memo)
    
    
    memo[st] = path
    return path


def word_break(st, di):
    
    if len(st) == 0: 
        print('Yay')
        return 1
    
    path = 0
    for item in di: 
        if st.startswith(item):
            print(st)
            print(item)
            temp, nst = st.split(item,1)
            path = path + word_break(nst, di)
    
    return path


st = 'RohitRohiniMungre'
di = ['Rohit' , 'Rohini', 'Roh' , 'it', 'ini', 'Mungre' , 'ABC']

print(word_break(st, di))
print(word_break_dp(st, di, {}))

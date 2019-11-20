def egg_drop(n,k, memo):
	mstr = str(n)+'~'+str(k)
	if mstr in memo:
		return memo[mstr]
	if n==1 or k==0 or k==1:
		memo[mstr] = k
		return k
	
	res = max(egg_drop(n-1, 0, memo), egg_drop(n, k-1, memo))
	for i in range(2,k):
		tmp = max(egg_drop(n-1, i-1, memo), egg_drop(n, k-i, memo))
		res = min(tmp,res)	
	memo[mstr] = 1+res
	return 1+res

n=2
k=100
print(egg_drop(n,k,{}))

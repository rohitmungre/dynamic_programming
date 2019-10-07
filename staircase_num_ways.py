step1 = 1
step2 = 2

end_height = 7

def num_ways_dp(end_height, step1, step2, memo):
	if end_height in memo:
		return memo[end_height]
	if end_height == 0 : 
		memo[end_height] = 1
		return 1
	if end_height < 0:
		memo[end_height] = 0
		return 0 	
	
	w1 = num_ways_dp(end_height - step1, step1, step2, memo)
	w2 = num_ways_dp(end_height - step2, step1, step2, memo)
	memo[end_height] = w1+w2	
	return w1+w2

def num_ways(end_height, step1, step2):
	if end_height == 0 : 
		return 1
	if end_height < 0:
		return 0 	
	
	w1 = num_ways(end_height - step1, step1, step2)
	w2 = num_ways(end_height - step2, step1, step2)
	
	return w1+w2

print(num_ways(end_height, step1, step2))
print(num_ways_dp(end_height, step1, step2, {}))

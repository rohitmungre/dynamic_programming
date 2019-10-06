arr = [4,6,1,3,8,4,6]

def max_increasing_sum_dp(arr, idx, memo):
	
	if idx in memo:
		return memo[idx]
		
	if idx < 0:
		memo[idx] = []
		return []
	
	if idx == 0:
		memo[idx] = [arr[0]]
		return [arr[0]]
		
	i = idx-1
	tmp_max = 0
	tmp_idx = -1
	
	while(i>=0):
		if arr[idx]>arr[i] and sum(max_increasing_sum(arr, i)) > tmp_max:
			tmp_max = sum(max_increasing_sum(arr, i)) 
			tmp_idx = i 
		i = i-1

	if tmp_idx <0:
		return [arr[idx]]
	
	prev_arr = max_increasing_sum(arr, tmp_idx)	
	memo[idx] = prev_arr + [arr[idx]]
	return prev_arr + [arr[idx]]

def mas_wrapper_dp(arr, idx):
	abs_max = 0
	abs_arr = []
	memo = {}
	for i in range(0,idx+1):
		if sum(max_increasing_sum_dp(arr, i, memo))>abs_max:
			abs_arr = max_increasing_sum_dp(arr,i, memo)
			abs_max = sum(abs_arr)
	return abs_arr


def max_increasing_sum(arr, idx):
	
	if idx < 0:
		return []
	
	if idx == 0:
		return [arr[0]]
		
	i = idx-1
	tmp_max = 0
	tmp_idx = -1
	
	while(i>=0):
		if arr[idx]>arr[i] and sum(max_increasing_sum(arr, i)) > tmp_max:
			tmp_max = sum(max_increasing_sum(arr, i)) 
			tmp_idx = i 
		i = i-1

	if tmp_idx <0:
		return [arr[idx]]
	
	prev_arr = max_increasing_sum(arr, tmp_idx)	
	return prev_arr + [arr[idx]]
	
def mas_wrapper(arr, idx):
	abs_max = 0
	abs_arr = []
	for i in range(0,idx+1):
		if sum(max_increasing_sum(arr, i))>abs_max:
			abs_arr = max_increasing_sum(arr,i)
			abs_max = sum(abs_arr)
	return abs_arr

print(max_increasing_sum(arr, 6))	
print(mas_wrapper(arr, 6))	
print(max_increasing_sum_dp(arr, 6, {}))	
print(mas_wrapper_dp(arr, 6))	

mat = [[2,0,-3,4],
	   [6,3,2,-1],
	   [5,4,7,3],
	   [2,-6,8,1]]
	   
start = (1,0)
end = (2,2)

def fill_sum_mat(mat):
	sum_mat = [[0 for i in range(0, len(mat[0])+1)] for j in range(0, len(mat)+1)]
	for i in range(0,len(mat)):
		for j in range(0,len(mat[0])):
			sum_mat[i+1][j+1] = sum_mat[i][j+1] + sum_mat[i+1][j] - sum_mat[i][j] + mat[i][j]
	return sum_mat
	
def sum_submat(mat, start, end):
	sum_mat = fill_sum_mat(mat)
	
	return sum_mat[end[0]+1][end[1]+1] + sum_mat[start[0]][start[1]] - sum_mat[start[0]][end[1]+1] - sum_mat[end[0]+1][start[1]]
	

print(fill_sum_mat(mat))

print(sum_submat(mat, start, end))

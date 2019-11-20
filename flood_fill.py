def flood_fill(arr, pos, old_color, new_color):
	arr[pos[0]][pos[1]] = new_color	
	up_pos, down_pos, left_pos, right_pos = get_neighbours(arr, pos)
	print(pos, up_pos, down_pos, left_pos, right_pos)

	if up_pos:
		if arr[up_pos[0]][up_pos[1]] == old_color:
			arr = flood_fill(arr, up_pos, old_color, new_color)
	if down_pos:
		if arr[down_pos[0]][down_pos[1]] == old_color:
			arr = flood_fill(arr, down_pos, old_color, new_color)
	if left_pos:
		if arr[left_pos[0]][left_pos[1]] == old_color:
			arr = flood_fill(arr, left_pos, old_color, new_color)
	if right_pos:
		if arr[right_pos[0]][right_pos[1]] == old_color:
			arr = flood_fill(arr, right_pos, old_color, new_color)
	
	return arr
	
def get_neighbours(arr, pos):
	up_pos = [0,0]
	up_pos[0] = pos[0]-1
	up_pos[1] = pos[1]
	
	down_pos = [0,0]
	down_pos[0] = pos[0]+1
	down_pos[1] = pos[1]
	
	left_pos = [0,0]
	left_pos[0] = pos[0]
	left_pos[1] = pos[1]-1
	
	right_pos = [0,0]
	right_pos[0] = pos[0]
	right_pos[1] = pos[1]+1
	
	if pos[0] == 0:
		up_pos = False
	if pos[0] == len(arr)-1:
		down_pos = False
	if pos[1] == 0:
		left_pos = False
	if pos[1] == len(arr[0])-1:
		right_pos = False
	return up_pos, down_pos, left_pos, right_pos



arr = [[0,0,0,0,0],[0,1,1,1,0],[1,1,1,0,0],[0,1,1,1,1],[1,2,2,2,2]]
pos = [1,1]
old_color = 1
new_color = 3
print(flood_fill(arr, pos, old_color, new_color))

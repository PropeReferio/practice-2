# This problem was asked by Amazon.
# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# For example, given the following matrix:

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]
# You should print out the following:

# 1
# 2
# 3
# 4
# 5
# 10
# 15
# 20
# 19
# 18
# 17
# 16
# 11
# 6
# 7
# 8
# 9
# 14
# 13
# 12

spiral = [(0, 1), (1, 0), (0, -1), (-1, 0)]
z = 0
direction = spiral[z]
#This might not work, direction might not change as z changes

visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
y, x = 0, 0

while True:
    # if all([all(lst) for lst in visited]): # Time: O(n**2), where n is total
    #  number of elements in matrix. We can get down to O(4n) by checking all 
    # 4 sides for visited before we move.
    #     break
    print(matrix[y][x])
    visited[y][x] = True
    if y + direction[0] >= len(matrix) or x + direction[1] >= len(matrix[0])\
or x + direction[1] < 0 or visited[y+direction[0]][x+direction[1]]:
        z = (z + 1) % 4 
        direction = spiral[z]
        
    y += direction[0]
    x += direction[1]
    if visited[y][x]:
        break
    #This is even better. If we've just changed direction because the next
    #node was visited or out of bounds, and the NEW next node is ALSO visited
    #or out of bounds, then we've visited every node. O(n).




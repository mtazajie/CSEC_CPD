# Read the matrix
matrix = [list(map(int, input().split())) for _ in range(5)]

# Find the position of '1'
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row, col = i, j
            break

# Calculate the minimum number of moves
moves = abs(row - 2) + abs(col - 2)

# Output the result
print(moves)

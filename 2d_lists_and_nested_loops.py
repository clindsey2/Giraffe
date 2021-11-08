
# 4 elements in the list, each of them also a list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
print(number_grid[2][1])
print("------------------")

# nested for loop, to print out each element
for row in number_grid:
    for col in row:
        print(col)

print("==================")

# print each element by indices
r = 0
c = 0
for row in number_grid:
    for c in range(len(row)):
        print(number_grid[r][c])
        c += 1
    r += 1

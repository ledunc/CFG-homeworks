def search_in_matrix(matrix, target):
    if len(matrix) == 0:
        print("This is not a valid matrix")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            # if target is in the matrix
            if matrix[i][j] == target:
                print(f"result = [{i}, {j}]")
                return [i, j]

    # if target doesn't exist in the matrix
    print("Element doesn't exist in the matrix")
    return [-1, -1]


matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target = 42

search_in_matrix(matrix, target)

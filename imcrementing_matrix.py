"""
0, 1, 2, 3, 4
1, 2, 3, 4, 5
2, 3, 4, 5, 6
3, 4, 5, 6, 7
4, 5, 6, 7, 8

matrix(5)
"""

def incrimenting_matrix(n):
    matrix = [[None for y in range(n)] for x in range(n)]
    counter = 0

    for idx, el in enumerate(matrix):
        for nested_idx, nested_el in enumerate(el):
            matrix[idx][nested_idx] = counter + nested_idx

        counter += 1

    return matrix


print(incrimenting_matrix(5))
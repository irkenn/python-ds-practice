def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    end = len(matrix[0])
    output = 0
    #first diagonal TL-to-BR
    for i in range(end):
        output += matrix[i][i]
    index_sum = 0
    #second diagonal BL-to-TR
    for j in reversed(range(end)): 
        output += matrix[index_sum][j]
        index_sum += 1
    return output

   
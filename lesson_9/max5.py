def max_sequence(seq):
    """
    Функция ищет пять соседних элементов списка, сумма значений которых максимальна.
    >>> max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
    [4, 4, 4, 3, 4]
    >>> max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
    [7, 2, 9, 2, 9]
    """
    c=[]
    for i in range(len(seq)-4):
        b=[seq[(i+j)] for j in range(5)]
        if sum(b)>sum(c):
            c=b;
    return c

if __name__ == '__main__':
    import doctest
    doctest.testmod()

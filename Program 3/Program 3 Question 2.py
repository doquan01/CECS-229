def my_lists(L):
    '''
    >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    >>> my_lists([0,3])
    [[], [1, 2, 3]]
    '''
    total = []
    for i in L:
        if(i == 0):
            k = []
            total.append(k)
        else:
            temp = []
            for j in range(i):
                temp.append(j+1)
            total.append(temp)
    return total
L = [1,2,4]
print(my_lists(L))

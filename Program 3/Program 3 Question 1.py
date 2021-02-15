def myFilter(L, num):
    '''
    Input:
      -L: a list of numbers
      -num: a positive integer
    Output:
      -a list of numbers not containing a multiple of num
    Examples:
      >>> myFilter([1,2,4,5,7],2)
      [1, 5, 7]
      >>> myFilter([10,15,20,25],10)
      [15, 25]
    '''
    temp =[]
    for i in L:
        if(i % num != 0):
            temp.append(i)
    return temp;

L = [1,2,4,5,7]
print(myFilter(L, 2))

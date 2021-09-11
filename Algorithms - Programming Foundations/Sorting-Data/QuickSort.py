# QuickSort algorithm

def quickSort(dataset, first , last):
    if first < last:
        # here we make partitions and get the pivot positon
        pivoteIdx = partition(dataset,first,last)
        # now we sort the two partition
        quickSort(dataset,first,pivoteIdx-1)
        quickSort(dataset,pivoteIdx+1,last)

def partition(data, first, last):

    pivotval = data[first]

    lower = first + 1
    upper = last

    done = False
    while not done:
        
        while lower <= upper and data[lower] <= pivotval:
            lower += 1
        
        while upper >= lower and data[upper] >= pivotval:
            upper -= 1
        
        if lower > upper :
            done = True
        else:
            tmp = data[lower]
            data[lower] = data[upper]
            data[upper] = tmp
    tmp = data[upper]
    data[upper] = data[first]
    data[first] = tmp

    return upper


list = [32,65,16,56,66,43,2,2,3,89,2,42,63,41]
print(list)
quickSort(list, 0, len(list)-1)
print(list)


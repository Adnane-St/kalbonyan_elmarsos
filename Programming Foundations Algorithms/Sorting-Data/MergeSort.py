# Merge Sort algorithm


def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2
        leftarr = data[:mid]
        rightarr = data[mid:]


        # TODO: recursion the both side until remain one item
        mergesort(leftarr)
        mergesort(rightarr)

        j=0
        i=0
        k=0

        # TODO: check small value in both side
        while i < len(leftarr) and j < len(rightarr):
            if(rightarr[j] < leftarr[i]):
                data[k] = rightarr[j]
                j += 1
            else:
                data[k] = leftarr[i]
                i += 1
            k += 1
        # TODO: left array remains
        while i <len(leftarr):
            data[k] = leftarr[i]
            i += 1
            k += 1
        # TODO: left array remains
        while j <len(rightarr):
            data[k] = rightarr[j]
            j += 1
            k += 1

list = [32,65,16,56,66,43,2,2,3,89,2,42,63,41]
print(list)
mergesort(list)
print(list)
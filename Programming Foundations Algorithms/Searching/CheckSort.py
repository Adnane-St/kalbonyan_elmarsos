#Cheking if an array is sorted

def isSort(list):
    return all(list[i] <= list[i+1] for i in range(len(list)-1))

print(isSort([1,5,9,15,25,42,58,69,77,90,190]
))
print(isSort([1,5,9,15,253,42,58,69,77,90,10]))
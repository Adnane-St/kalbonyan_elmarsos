# Bubble sort algorithm

def bubbleSort(data):
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if(data[j] > data[j+1]):
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
        print("Changes : ",data)

list = [32,65,16,56,66,43,2,2,3,89,2,42,63,41]
bubbleSort(list)
print("Result : ",list)
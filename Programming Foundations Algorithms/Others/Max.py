# Find the max value in a list 


def findMax(list):

    if(len(list) == 1):
        return list[0]
    
    itm1 = list[0]
    itm2 = findMax(list[1:])
    
    if itm1 > itm2:
        return itm1
    else:
        return itm2

list = [32,65,98,16,42,63,41]
print(findMax(list))
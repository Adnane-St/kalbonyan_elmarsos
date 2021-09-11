# Ordred list search item
# by using binary search 
# My solution
def search(itm,list,first,last):
    mid = first + last // 2
    if list[mid] == itm:
        return mid
    elif list[mid] < itm:
        return search(itm,list,mid,last)
    else:
        return search(itm,list,first,mid)

list = [1,5,9,15,25,42,58,69,77,90,190]

print(search(25,list,0,len(list)-1))
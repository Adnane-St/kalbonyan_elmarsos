# Search an item in Unordred list 

list = [32,65,16,42,63,41]

# My solution
def search(itm,list):
    for i in range(len(list)):
        if itm == list[i]:
            return i
    return None

print(search(412,list))
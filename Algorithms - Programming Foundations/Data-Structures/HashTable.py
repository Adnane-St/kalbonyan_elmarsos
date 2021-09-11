#hash is dict in python and objects in Js

# create a hashtable with python dict
hTable1= dict({"name":"myName","id":2234523,"gg":"good game"})
print(hTable1)

# try to add key and value
hTable2 = {"name":"kingMan"}
hTable2["wifeName"] = "queenBerry"

# print all item in hashTable
for item,val in hTable2.items():
    print(item,val)
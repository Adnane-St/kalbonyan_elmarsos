


from typing import Counter


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
    def getVal(self):
        return self.val
    def setVal(self,val):
        self.val = val
    def getNext(self):
        return self.next
    def setNext(self,next):
        self.next = next

#the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.count = 0
    def get_count(self):
        return self.count
    def insert(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node
        self.count += 1
    def find(self,val):
        item = self.head
        while(item != None):
            if(item.getVal() == val):
                return item
            else:
                item = item.getNext()
        return None
    def deleteAt(self,idx):
        if idx>self.count-1:
            return
        elif idx == 0:
            self.head = self.head.getNext()
        else:
            tmpIdx = 0
            prevNode=self.head
            while(tmpIdx < idx-1):
                prevNode = prevNode.getNext()
                tmpIdx += 1
            prevNode.setNext(prevNode.getNext().getNext())
            self.count -= 1 
    def dump_list(self):
        count = 0
        itm=self.head
        while(count < self.count):
            print(itm.val)
            itm=itm.getNext()
            count +=1

itemList = LinkedList()
itemList.insert(25)
itemList.insert(56)
itemList.insert(67)
itemList.insert(10)
itemList.insert(23)

itemList.dump_list()

print("Item count: ", itemList.get_count())
itemList.deleteAt(4)
print("Item count: ", itemList.get_count())
print("Finding Item: ", itemList.find(25))
print("Finding Item: ", itemList.find(10))
itemList.dump_list()


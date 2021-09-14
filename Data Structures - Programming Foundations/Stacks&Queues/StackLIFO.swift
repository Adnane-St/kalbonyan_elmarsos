//this is swift class for lofi stacks
class Stack {
    var stackArray = [String]()//Initiating our array
    //push
    func push(item:String) {
        self.stackArray.append(item)
    }
    func pop()->String? {
        if self.stackArray.last != nil {
            let lastString = self.stackArray.last
            self.stackArray.removeLast()
            return lastString!
        } else {
            return nil
        }
    }
    
    func peek() -> String? {
        if self.stackArray.last != nil {
            return self.stackArray.last
        } else {
            return nil
        }
    }
}

var deck:Stack = Stack()
deck.push(item:"Ma,Dz,Egp,Lyb,Tu")
print(deck.pop())
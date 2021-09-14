class Queue {
    var queueArray = [String]()
    
    func enqueue(item: String) {
        self.queueArray.append(item)
    }
    
    func dequeue() -> String? {
        if self.queueArray.first != nil {
            let firstString = self.queueArray.first
            self.queueArray.removeFirst()
            return firstString!
        } else {
            return nil
        }
    }
    
    func peek() -> String? {
        if self.queueArray.first != nil {
            return self.queueArray.first
        } else {
            return nil
        }
    }
}

var myQueue = Queue() //Create brand new Queue

// Here i have append items to the queue
myQueue.enqueue(item: "Sorry")
myQueue.enqueue(item: "Adnane")
myQueue.enqueue(item: "Ahmed")

//Here is the output of our items
print(myQueue.peek()!)
print(myQueue.peek()!)
print(myQueue.dequeue()!)
print(myQueue.peek()!)
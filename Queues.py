queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)

from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
print("\nQueue after removing elements")
print(q)

from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())

# With linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    # append
    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        return
    
    # REMOVE
    def dequeue(self):
        if self.front is None:
            print('your Queue is empty')
            return
        data = self.rear.data
        while True:
            if self.front == self.rear:
                self.front = None
                self.rear = None
                break
            else:
                self.front = self.front.next
        return data
    
    # The front
    def peek(self):
        if self.front is None:
            return None
        return self.front.data
    
    def length(self):
        if self.front is None:
            return 0
        cur_node = self.front
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count
    
    def display(self):
        if self.front is None:
           return None
        cur_node = self.front
        while cur_node is not None:
            print(cur_node.data, end=' -> ')
            cur_node = cur_node.next
        print('None')
        return

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

queue.display() 

print("Peek:", queue.peek()) 

print("Dequeued:", queue.dequeue())

queue.display() 


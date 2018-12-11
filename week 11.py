

class Node:
    def __init__(self, init_data):
       self.data = init_data
       self.next = None
       self.previous = None

class Queue:
    def __init__(self):
        self.front = None
        self.back = None
    def enqueue(self, x):
        #implements this: adds a new Node with x to back, so back points to this node,
        #while the previous of the old back's Node must point to the this new node and
        #this new Node's next must point to the old back
        new_node = Node(x)
        new_node.next = self.front
        new_node.previous = self.back
        self.back = new_node

    def dequeue(self):
        #implement this: returns the data of the Node pointed to by front and
        #makes new front point to the previous of the Node pointed to by old front
        return self.front.data
        self.back = self.front.next

    def is_empty(self):
        #implement this
        if self.front == None:
            return True
        else:
            return False


#NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input: exec(line)
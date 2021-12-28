class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
    #Complete this method
        if head is None:
            head = Node(data)
            self.tail = head
            print(str(head) + " <-- This is the object, the pointer of the first element")
        else: 
            node = Node(data)    
            # node has now the data and next attributes of the class Node
            print(str(node) + " <-- This is the new object, the pointer")
            print(str(node.data) + " <-- This is the data we just assigned")
            print(str(node.next) + " <-- This is the next attribute which is assigned to None")
            
            self.tail.next = node
            # the object with the "tail" attribute, which is the head, has at the 
            # same time the "next" attribute.
            
            # With the assignation, we are saying that the "next" value of the object before this new one
            # it will be the new node with the new data
            print(str(self.tail.next) + " <-- This is the new node we are inserting")
            print(str(self.tail) + " <-- This is the node before the inserted")
            self.tail = node
            # And now, this new node is the tail of the Linked list
            print(str(self.tail) + " <-- Now we just uploaded the tail element as the last element we inserted")
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 
from queue import Queue

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        levels = Queue(maxsize=100)
        data_nodes = []
        levels.put(root)
        while (levels.qsize() != 0):
            node = levels.get()
            data_nodes.append(node.data)
            if (node.left != None):
                levels.put(node.left)
            if (node.right != None):
                levels.put(node.right)
        for i in data_nodes:
            print(i, end=" ")
T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

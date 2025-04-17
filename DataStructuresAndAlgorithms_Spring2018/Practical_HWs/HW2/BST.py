import sys
sys.setrecursionlimit(1000000)
class Node:
    def __init__(self, val, daddy):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.daddy = daddy
        self.height = 0

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def getChildren(self):
        children = []
        if (self.leftChild != None):
            children.append(self.leftChild)
        if (self.rightChild != None):
            children.append(self.rightChild)
        return children


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val, None)

    def insert(self, val):
        if (self.root is None):
            self.setRoot(val)
            self.root.height = 1
        else:
            self.insertNode(self.root, val, 2)

    def insertNode(self, currentNode, val, newHeight):
        if (val <= currentNode.val):
            if (currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val, newHeight + 1)
            else:
                currentNode.leftChild = Node(val, currentNode)
                currentNode.leftChild.height = newHeight
                self.updateDaddies(currentNode.leftChild, currentNode.leftChild.height)


        elif (val > currentNode.val):
            if (currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val, newHeight + 1)
            else:
                currentNode.rightChild = Node(val, currentNode)
                currentNode.rightChild.height = newHeight
                self.updateDaddies(currentNode.rightChild, currentNode.rightChild.height)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if (currentNode is None):
            self.insert(val)
            return 0
        elif (val == currentNode.val):
             return currentNode.height
        elif (val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
    def updateDaddies(self, node, num):
        if(node.daddy == None):
            return
        node.daddy.height += num
        self.updateDaddies(node.daddy, num)


bst = BST()
Instra = int(input())
for i in range(Instra):
    number = int(input())
    sout = bst.find(number)
    if(sout != 0):
        print(str(sout))
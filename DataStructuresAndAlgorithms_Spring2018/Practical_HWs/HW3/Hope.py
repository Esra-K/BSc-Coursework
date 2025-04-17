class Node:
    def __init__(self):
        self.mark = False
        self.edges = [None] * 2 # A list of Edges exiting from this node
    def isFree(self):
        return self.edges == [None, None]
    def isLeaf(self):
        return self.mark

def trie_insert(node, string, idx = 0):
    if idx == 32:
        node.mark = True # marking the node
        return
    e = (string >> (31-idx)) & 1
    if node.edges[e] is None:
        node.edges[e] = Node()
    trie_insert(node.edges[e], string, idx+1)

def trie_delete(node, key, level):
    if(node):
        if level == 32:
            if node.mark:
                node.mark = False
            return node.isFree()
        else:
            index = (key >> (31 - level)) & 1
            if(trie_delete(node.edges[index], key, level + 1)):
                node.edges[index] = None
                return (not node.isLeaf() and node.isFree())
    return False

def findMaxXor(node, key):
    maxXor = 0
    for j in range(31, -1, -1):
        b = key >> j & 1
        if(b == 0):
            if(node.edges[1]):
                maxXor += 2**j
                node = node.edges[1]
            elif(node.edges[0]):
                node = node.edges[0]
        else:
            if (node.edges[0]):
                maxXor += 2 ** j
                node = node.edges[0]
            elif(node.edges[1]):
                node = node.edges[1]
    return maxXor

queries = int(input())
array = Node()
trie_insert(array,0, 0)
for i in range(queries):
    Input = input()
    instruction = Input[0:3]
    number = int(Input[4: len(Input)])
    if(instruction == 'add'):
        trie_insert(array, number, 0)
    elif(instruction == 'rem'):
        trie_delete(array, number, 0)
    elif(instruction == 'ans'):
        print(findMaxXor(array, number))
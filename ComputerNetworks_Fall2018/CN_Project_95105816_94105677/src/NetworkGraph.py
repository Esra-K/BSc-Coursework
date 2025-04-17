import time
import random
from random import randint

class GraphNode:
    # alive field
    def __init__(self, address):
        """
        :param address: (ip, port)
        :type address: tuple
        """
        self.isAlive = False
        self.address = address
        self.parent = None
        self.children = []

    def set_parent(self, parent):
        self.parent = parent

    def set_address(self, new_address):
        self.address = new_address

    def __reset(self):
        del self

    def add_child(self, child):
        self.children.append(child)


class NetworkGraph:
    def __init__(self, root):
        self.root = root
        root.isAlive = True
        self.nodes = [root]

    def find_live_node(self, sender):

        """
        Here we should find a neighbour for the sender.
        Best neighbour is the node who is nearest the root and has not more than one child.

        Code design suggestion:
            1. Do a BFS algorithm to find the target.

        Warnings:
            1. Check whether there is sender node in our NetworkGraph or not; if exist do not return sender node or
               any other nodes in its sub-tree.

        :param sender: The node address we want to find best neighbour for it.
        :type sender: tuple

        :return: Best neighbour for sender.
        :rtype: GraphNode
        """
        return self.find_live_node_2(sender, self.root)

    def find_live_node_2(self, sender, node):
        if len(node.children) <= 1 and node.isAlive:
            return node
        else:
            for child in node.children:
                if not (self.find_live_node_2(sender, child) is None):
                    # print("child" , child.address[1])
                    return child
        return None

    def find_node(self, ip, port):
        ip, port = self.uglify(ip, port)
        return self.find_node_2(ip, port, self.root)

    def find_node_2(self, ip, port, node):
        if node.address[0] == ip and node.address[1] == port:
            return node
        else:
            '''print(node.address[0], ip)'''
            # print(node.address[1], port)
        for child in node.children:
            n = self.find_node_2(ip, port, child)
            if not (n is None):
                return n
        return None

    def turn_on_node(self, node_address):
        self.find_node(*node_address).isAlive = True

    def turn_off_node(self, node_address):
        self.find_node(*node_address).isAlive = False

    def remove_node(self, node_address):
        self.remove_node_2(node_address, self.root)

    def remove_node_2(self, node_address, node):
        found = self.find_node(node_address[0], node_address[1])
        if not (found is None):
            print("I'm node", node_address)
            self.deleteUtil(self.find_node(node_address[0], node_address[1]))
            found = None

    def deleteUtil(self, node):
        for child in node.children:
            self.deleteUtil(child)
        node.isAlive = False
        node.parent.children.remove(node)
        node.parent = None

    def add_node(self, ip, port):
        ip, port = self.uglify(ip, port)
        papa = None
        queue = []
        queue.append(self.root)
        flag = False
        while queue:
            s = queue.pop(0)
            if len(s.children) <= 1 and s.isAlive:
                papa = s
                break
            for i in s.children:
                queue.append(i)
        node = GraphNode((ip, port))
        node.parent = papa
        papa.children.append(node)
        node.isAlive = True
        return papa.address

    def customPrint(self, node):
        print("address:", node.address, "alive:", node.isAlive, "parent:",
              node.parent.address[1] if not (node.parent is None) else node.parent, "children:",
              [child.address[1] for child in node.children])
        for child in node.children:
            self.customPrint(child)

    def print_self(self):
        self.customPrint(self.root)

    def uglify(self, ip, port):
        """
        Change parse_ip and parse_port output to acceptable format.

        :param ip: input ip
        :param port: input port
        :return: address (ip, port)
        """

        return '.'.join([str(int(part)) for part in ip.split('.')]), int(port)
ip = '127.0.0.1'
g = NetworkGraph(GraphNode(('127.0.0.1', 5000)))

g.add_node(ip, 6000)
g.add_node(ip, 7000)
g.add_node(ip, 8000)

g.print_self()

g.remove_node((ip, 6000))

print('\n')

g.print_self()

g.add_node(ip, 6000)

print('\n')

g.print_self()
g.add_node(ip, 8000)

print('\n')

g.print_self()


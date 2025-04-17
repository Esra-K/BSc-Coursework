class GraphNode:
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


def uglify(ip, port):
    """
    Change parse_ip and parse_port output to acceptable format.

    :param ip: input ip
    :param port: input port
    :return: address (ip, port)
    """

    return '.'.join([str(int(part)) for part in ip.split('.')]), int(port)


class NetworkGraph:
    def __init__(self, root):
        self.root = root
        root.isAlive = True
        self.nodes = [root]

    def find_node(self, ip, port):
        ip, port = uglify(ip, port)
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
            self.deleteUtil(self.find_node(node_address[0], node_address[1]))
            found = None

    def deleteUtil(self, node):
        for child in node.children:
            self.deleteUtil(child)
        node.isAlive = False
        node.parent.children.remove(node)
        node.parent = None

    def add_node(self, ip, port):
        ip, port = uglify(ip, port)
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
        print("\taddress:", node.address, "alive:", node.isAlive, "parent:",
              node.parent.address[1] if not (node.parent is None) else node.parent, "children:",
              [child.address[1] for child in node.children])
        for child in node.children:
            self.customPrint(child)

    def print_self(self):
        self.customPrint(self.root)



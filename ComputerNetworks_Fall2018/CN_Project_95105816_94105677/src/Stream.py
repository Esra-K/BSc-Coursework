from src.tools.simpletcp.tcpserver import TCPServer

import random
from src.tools.Node import Node
import threading


class Stream:

    def __init__(self, ip, port):
        """
        The Stream object constructor.

        Code design suggestion:
            1. Make a separate Thread for your TCPServer and start immediately.


        :param ip: 15 characters
        :param port: 5 characters
        """
        self.nodes = []
        self.out_messages = dict()

        # This is tcpserver input buffer.
        self._server_in_buf = []

        def callback(address, queue, data):
            """
            The callback function will run when a new data received from server_buffer.

            :param address: Source address.
            :param queue: Response queue.
            :param data: The data received from the socket.
            :return:
            """
            queue.put(bytes('ACK', 'utf8'))
            self._server_in_buf.append(data)
            print(self._server_in_buf)

        class TCPThread(threading.Thread):
            def __init__(self, tcpserver):
                threading.Thread.__init__(self)
                self.tcpserver = tcpserver

            def run(self):
                self.tcpserver.run()

        self.tcpserver = TCPServer(ip, port, callback)
        TCPThread(self.tcpserver).start()

    def get_server_address(self):
        """

        :return: Our TCPServer address
        :rtype: tuple
        """
        return self.tcpserver.ip, self.tcpserver.port

    def clear_in_buff(self):
        """
        Discard any data in TCPServer input buffer.

        :return:
        """
        self._server_in_buf.clear()

    def add_node(self, server_address, set_register_connection=False):
        """
        Will add new a node to our Stream.

        :param server_address: New node TCPServer address.
        :param set_register_connection: Shows that is this connection a register_connection or not.

        :type server_address: tuple
        :type set_register_connection: bool

        :return:
        """

        if self.get_node_by_server(server_address[0], server_address[1]) is not None:
            return
        self.nodes.append(Node(server_address, set_register=set_register_connection))

    def remove_node(self, node):
        """
        Remove the node from our Stream.

        Warnings:
            1. Close the node after deletion.

        :param node: The node we want to remove.
        :type node: Node

        :return:
        """
        # node = self.get_node_by_server(address[0], address[1])
        # if node is None:
        #     return
        self.nodes.remove(node)
        node.close()

    def get_node_by_server(self, ip, port):
        """

        Will find the node that has IP/Port address of input.

        Warnings:
            1. Before comparing the address parse it to a standard format with Node.parse_### functions.

        :param ip: input address IP
        :param port: input address Port

        :return: The node that input address.
        :rtype: Node
        """
        for node in self.nodes:
            if Node.parse_ip(node.server_ip) == Node.parse_ip(ip):
                if Node.parse_port(node.server_port) == Node.parse_port(port):
                    return node
        return None

    def add_message_to_out_buff(self, address, message):
        """
        In this function, we will add the message to the output buffer of the node that has the input address.
        Later we should use send_out_buf_messages to send these buffers into their sockets.

        :param address: Node address that we want to send the message
        :param message: Message we want to send

        Warnings:
            1. Check whether the node address is in our nodes or not.

        :return:
        """
        existence = False
        for node in self.nodes:
            if node.server_port == address[1] and node.server_ip is address[0]:
                if not node.client.closed:
                    n = node
                    existence = True
                else:
                    self.remove_node(node)
        if not existence:
            return
        key = address[0] + str(address[1])
        try:
            self.out_messages[key].append(message)
        except KeyError:
            self.out_messages[key] = [message]

        self.send_messages_to_node(n)

    def read_in_buf(self):
        """
        Only returns the input buffer of our TCPServer.

        :return: TCPServer input buffer.
        :rtype: list
        """
        return self._server_in_buf

    def send_messages_to_node(self, node):
        # Node.add_to_buffer
        """
        Send buffered messages to the 'node'

        Warnings:
            1. Insert an exception handler here; Maybe the node socket you want to send the message has turned off and
            you need to remove this node from stream nodes.

        :param node:
        :type node Node

        :return:
        """
        # print(address, self.nodes[0].server_port)
        # node = self.get_node_by_server(address[0], address[1])
        # if node is None:
        #     return
        key = node.server_ip + str(node.server_port)
        try:
            for msg in self.out_messages[key]:
                node.add_message_to_out_buff(msg)

            del self.out_messages[key]

        except Exception:
            self.remove_node(node)

    def send_out_buf_messages(self, only_register=False):
        # Node.send_messages()
        """
        In this function, we will send whole out buffers to their own clients.

        :return:
        """
        for node in self.nodes:
            if not only_register or node.is_register:
                node.send_message()


ip = '127.0.0.1'
a2 = (ip, 5000)
a1 = (ip, 6000)
s1 = Stream(ip, 6000)
s2 = Stream(ip, 5000)
s1.add_node(a2)
s2.add_node(a1)

s1.add_message_to_out_buff(a2, 'hi')
s2.add_message_to_out_buff(a1, 'hello')
s1.send_out_buf_messages()
s2.send_out_buf_messages()
s1.add_message_to_out_buff(a2, 'hi2')
s2.add_message_to_out_buff(a1, 'hello2')
s1.send_out_buf_messages()
s2.send_out_buf_messages()
s1.add_message_to_out_buff(a2, '3')
s2.add_message_to_out_buff(a1, 'hello3')

s1.remove_node(a2)
s1.send_out_buf_messages()
s2.send_out_buf_messages()

# gulfStream = []
# k = 7
# addresses = [i for i in range(5000, 5000 +k)]
# for i in range(5000, 5000 + k):
#     s = Stream(ip, i)
#     gulfStream.append(s)
# messages = [[]*(k-1)]*k
# for i in range(k):
#     for j in range(k - 1):
#         a = random.randint(1,1000)
#         messages[i].append("hello" + str(a))
# for i in range(k):
#     for j in range(k):
#         gulfStream[i].add_node((ip, addresses[j]))
#
#
#
# '''for i in range(k):
#     print(len(gulfStream[i].nodes))'''
#
# for i in range(k):
#     for j in range(k):
#         if i == j:
#             continue
#         gulfStream[i].add_message_to_out_buff((ip, addresses[j]),messages[i][j])
#
# # for i in range(k):
# #     for j in range(k - 1):
# #         if i == j:
# #             continue
#         # gulfStream[i].send_messages_to_node((ip, addresses[j]))
# for i in range(3):
#     rnd1 = random.randint(0,k - 1)
#     rnd2 = random.randint(0,k - 1)
#     gulfStream[rnd1].remove_node((ip, addresses[rnd2]))
#     print(rnd1 +1,rnd2 + 1)
#
# for i in range(k):
#     for j in range(k - 1):
#         gulfStream[i].send_out_buf_messages()
#
#
# for i in range(k):
#     gulfStream[i].remove_node((ip, addresses[i]))
#
#
# # # # # error

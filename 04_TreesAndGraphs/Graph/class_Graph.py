##############################################################################
# Linked List Class
##############################################################################

from class_Node import Node


class Graph(object):
    def __init__(self, nodes=[None]):
        self.__nodes = nodes

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def head(self, node):
        self.__head = node



##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    NodeA = Node()

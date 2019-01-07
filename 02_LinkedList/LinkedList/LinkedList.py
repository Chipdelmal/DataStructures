##############################################################################
# Linked List Class
##############################################################################

import Node as node


class LinkedList:
    def __init__(self, head=None):
        # Should be changed to take an array for initialization
        self.__head = head

    def getHead(self):
        return self.__head

    def __setHead(self, head):
        self.__head = head

    def traverseList(self):
        tempNode = self.__head
        while tempNode.getNext() is not None:
            tempNode = tempNode.getNext()
        return tempNode

    def printTraverseList(self):
        tempNode = self.__head
        print(tempNode.getData())
        while tempNode.getNext() is not None:
            tempNode = tempNode.getNext()
            print(tempNode.getData())

    def addTail(self, value):
        tempNode = node.Node(value, None)
        tail = self.traverseList()
        tail.setNext(tempNode)

    def addHead(self, value):
        tempNode = node.Node(value, self.__head)
        self.__setHead(tempNode)

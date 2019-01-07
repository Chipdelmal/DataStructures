##############################################################################
# Linked List Class
##############################################################################

import Node as node


class LinkedList:
    def __init__(self, head=None):
        self.__head = head

    def getHead(self):
        return self.__head

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

    def __addNode(self, newNode):
        tail = self.traverseList()
        tail.setNext(newNode)

    def addTail(self, value):
        tempNode = node.Node(value, None)
        self.__addNode(tempNode)

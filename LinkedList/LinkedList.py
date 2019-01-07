##############################################################################
# Linked List Class
##############################################################################

import Node as node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def getHead(self):
        return self.head

    def traverseList(self):
        tempNode = self.head
        while tempNode.getNext() is not None:
            tempNode = tempNode.getNext()
        return tempNode

    def printTraverseList(self):
        tempNode = self.head
        print(tempNode.getData())
        while tempNode.getNext() is not None:
            tempNode = tempNode.getNext()
            print(tempNode.getData())

    def addNode(self, newNode):
        tail = self.traverseList()
        tail.setNext(newNode)

    def addValue(self, value):
        tempNode = node.Node(value, None)
        self.addNode(tempNode)

##############################################################################
# Linked List Class
##############################################################################

from class_Node import Node


class LinkedList(object):
    def __init__(self, values=[None]):
        tnode = Node(values[0], None)
        self.__head = tnode
        for i in range(1, len(values)):
            self.addTail(values[i])

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, node):
        self.__head = node

    def traverseList(self):
        tempNode = self.head
        while tempNode.next is not None:
            tempNode = tempNode.next
        return tempNode

    def printTraverseList(self):
        tempNode = self.head
        print(tempNode.data)
        while tempNode.next is not None:
            tempNode = tempNode.next
            print(tempNode.data)

    def addTail(self, value):
        tempNode = Node(value, None)
        tail = self.traverseList()
        tail.next = tempNode

    def addHead(self, value):
        tempNode = Node(value, self.head)
        self.head = tempNode


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    llist = LinkedList([1, 2, 3, 2, 1])
    llist.head.data
    llist.printTraverseList()
    llist.addTail(10)
    llist.printTraverseList()
    llist.addHead(10)
    llist.printTraverseList()

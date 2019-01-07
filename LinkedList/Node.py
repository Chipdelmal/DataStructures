##############################################################################
# Node Class
##############################################################################


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next=None):
        self.next = next

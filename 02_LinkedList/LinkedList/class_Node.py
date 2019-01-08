##############################################################################
# Node Class
##############################################################################


class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def getData(self):
        return self.__data

    def getNext(self):
        return self.__next

    def setData(self, data):
        self.__data = data

    def setNext(self, next=None):
        self.__next = next

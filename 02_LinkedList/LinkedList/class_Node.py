##############################################################################
# Node Class
##############################################################################


class Node(object):
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    @property
    def data(self):
        return self.__data

    @property
    def next(self):
        return self.__next

    @data.setter
    def data(self, data):
        self.__data = data

    @next.setter
    def next(self, next=None):
        self.__next = next

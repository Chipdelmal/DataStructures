##############################################################################
# Node Class
##############################################################################


class Node(object):
    def __init__(self, data, links=None):
        self.__data = data
        self.__links = links

    @property
    def data(self):
        return self.__data

    @property
    def links(self):
        return self.__links

    @data.setter
    def data(self, data):
        self.__data = data

    @links.setter
    def links(self, links=None):
        self.__links = links

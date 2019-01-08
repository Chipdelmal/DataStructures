import LinkedList as ll

node = ll.Node(10,None)
node.data = 20
node.next

# class LinkedList(object):
#     def __init__(self, values=[None]):
#         tnode = ll.Node(10, None)
#         print(tnode.data)
#         self.__head = tnode
#
#     @property
#     def head(self):
#         return self.__head


llist = ll.LinkedList([1,2,3,2,1])
llist.head.data

llist.printTraverseList()

llist.addTail(20)
llist.printTraverseList()
llist.addTail(30)
llist.addTail(20)
llist.printTraverseList()

llist.addHead(100)
llist.printTraverseList()

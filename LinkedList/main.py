import LinkedList as ll
import Node as n

head = n.Node(10, None)
llist = ll.LinkedList(head)
llist.addTail(20)
llist.printTraverseList()
llist.addTail(30)
llist.addTail(20)
llist.printTraverseList()

llist.addHead(100)
llist.printTraverseList()

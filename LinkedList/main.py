import LinkedList as ll
import Node as n

head = n.Node(10, None)
llist = ll.LinkedList(head)
llist.addValue(20)
llist.printTraverseList()
llist.addValue(30)
llist.addValue(20)
llist.printTraverseList()

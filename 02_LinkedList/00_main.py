import LinkedList as ll

node = ll.Node(10,None)
node.data = 20
node.next


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

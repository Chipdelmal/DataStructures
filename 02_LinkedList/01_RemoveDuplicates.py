from LinkedList import LinkedList


class LinkedList_RemoveDuplicates(LinkedList):
    def __init__(self, values=[None]):
        super(LinkedList_RemoveDuplicates, self).__init__(values)

    def removeDuplicatesHash(self):
        if (self.head is None):
            # Linked list is empty
            return None
        else:
            # Prime the list with the head, and the set with present values
            currentNode = self.head
            valuesPresent = {currentNode.data}
            nextNode = currentNode.next
            while nextNode is not None:
                currentNode = nextNode
                nextNode = currentNode.next
                valuesPresent.add(currentNode.data)
            return valuesPresent
    def removeDuplicatesNoBuffer():
        return 1


llist2 = LinkedList_RemoveDuplicates([2, 3, 4, 3, 2, 1])
#llist2.printTraverseList()
llist2.removeDuplicatesHash()
llist2.printTraverseList()

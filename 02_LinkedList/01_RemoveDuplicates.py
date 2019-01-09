from LinkedList import LinkedList


class LinkedList_RemoveDuplicates(LinkedList):
    def __init__(self, values=[None]):
        super(LinkedList_RemoveDuplicates, self).__init__(values)

    def removeDuplicatesHash(self):
        if self.head is None:
            # Linked list is empty
            return None
        else:
            # Prime the list with the head, and the set with present values
            currentNode = self.head
            valuesPresent = {currentNode.data}
            # Iterate the list changing the pointers if values are present
            while currentNode.next is not None:
                nextNode = currentNode.next
                print("c: ", currentNode.data, "::", "n: ", nextNode.data)
                if nextNode.data in valuesPresent:
                    print("present: ", nextNode.data)
                    # Would need to destruct next here if it was C++
                    while nextNode.data in valuesPresent:
                        currentNode.next = nextNode.next
                        currentNode = currentNode.next
                else:
                    valuesPresent.add(nextNode.data)
                    currentNode = currentNode.next

    def removeDuplicatesNoBuffer():
        return 1


llist2 = LinkedList_RemoveDuplicates([2, 3, 4, 3, 2, 1])
#llist2.printTraverseList()
llist2.removeDuplicatesHash()
llist2.printTraverseList()

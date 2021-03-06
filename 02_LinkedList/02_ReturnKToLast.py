from LinkedList import LinkedList
from LinkedList import Node


class LinkedList_KToLast(LinkedList):
    def __init__(self, values=[None]):
        super(LinkedList_KToLast, self).__init__(values)

    def returnKToLast(self, k):
        if (self.head is None) or (k < 0):
            # Linked list is empty
            return Node("Linst is Empty or Index is Negative")
        runner = self.head
        current = self.head

        # Advance runner until it hits 'k' distance or runs out of the list
        counter = 1
        while (counter <= k + 1):
            if runner is None:
                return Node("Index is out of range")
            else:
                runner = runner.next
            counter = counter + 1
        # Move both probes until the runner hits the end
        while (runner is not None):
            current = current.next
            runner = runner.next
        return current


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    llist = LinkedList_KToLast([2, 3, 4, 3, 3, 1])
    node = llist.returnKToLast(10)
    print(node.data)

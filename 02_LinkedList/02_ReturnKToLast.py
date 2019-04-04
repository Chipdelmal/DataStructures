from LinkedList import LinkedList


class LinkedList_KToLast(LinkedList):
    def __init__(self, values=[None]):
        super(LinkedList_KToLast, self).__init__(values)

    def returnKToLast(self, k):
        if (self.head is None):
            # Linked list is empty
            return None

        runner = self.head
        current = self.head

        # Advance runner until it hits 'k' distance or runs out of the list
        counter = 0
        while (counter < k):
            if runner.next is None:
                return None
            else:
                runner = runner.next
            counter = counter + 1
        #
        while (runner is not None):
            current = current.next
            runner = runner.next
        return current


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    llist = LinkedList_KToLast([2, 3, 4, 3, 3, 1])
    node = llist.returnKToLast(5)
    print(node.data)

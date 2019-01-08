from LinkedList import LinkedList


class LinkedList_RemoveDuplicates(LinkedList):
    def __init__(self, values=[None]):
        super(LinkedList_RemoveDuplicates, self).__init__(values)
        #super().__init__(self, values=[None])

    # def removeDuplicatesHash():
    #     return 1
    # def removeDuplicatesNoBuffer():
    #     return 1

llist2 = LinkedList_RemoveDuplicates([2,3,4])
llist2.printTraverseList()

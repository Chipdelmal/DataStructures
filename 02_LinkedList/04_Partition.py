from LinkedList import LinkedList


def partition(linkedList, threshold):
    probe = linkedList.head
    if probe is not None:
        partitioned = LinkedList([probe.data])
        while (probe.next is not None):
            probe = probe.next
            data = probe.data
            if data < threshold:
                partitioned.addHead(data)
            else:
                partitioned.addTail(data)
    else:
        partitioned = LinkedList([None])
    return partitioned


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    llist = LinkedList([2, 3, 4, 5, 10, 11, 3, 3, 1])
    partitioned = partition(llist, 5)
    partitioned.printTraverseList()

from LinkedList import LinkedList


def carryAndRemainder(sA, sB, carry, base=10):
    sum = (sA + sB + carry)
    totals = [sum // base, sum % base]
    return totals


def sumNonEmptyLists(llA, llB, base=10):
    # Prime the list
    sA = llA.head.data
    sB = llB.head.data
    carry, remainder = carryAndRemainder(sA, sB, 0)
    llC = LinkedList([remainder])

    probeA = llA.head.next
    probeB = llB.head.next

    while (probeA is not None) or (probeB is not None):
        if (probeA is None):
            carry, remainder = carryAndRemainder(
                0, probeB.data, carry, base=base
            )
            llC.addTail(remainder)
            probeB = probeB.next
        elif (probeB is None):
            carry, remainder = carryAndRemainder(
                probeA.data, 0, carry, base=base
            )
            llC.addTail(remainder)
            probeA = probeA.next
        else:
            carry, remainder = carryAndRemainder(
                probeA.data, probeB.data, carry, base=base
            )
            llC.addTail(remainder)
            probeA = probeA.next
            probeB = probeB.next
    return llC


def sumLinkedLists(llA, llB, base=10):
    if (llA.head.data is None):
        return llB
    elif (llB.head.data is None):
        return llA
    else:
        return sumNonEmptyLists(llA, llB)


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    llA = LinkedList([3, 1, 2])
    llB = LinkedList([1, 9, 5, 8])

    llC = sumLinkedLists(llA, llB)
    llC.printTraverseList()

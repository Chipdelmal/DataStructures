from LinkedList import Node


def deleteNode(deletionNode):
    current = deletionNode
    next = deletionNode.next
    while (current is not None) and (next is not None):
        current.data = next.data
        # Move
        current = next
        next = next.next
    current.next = None
    return True


##############################################################################
# Test and Debug
##############################################################################
if __name__ == '__main__':
    nodeD = Node(1, None)
    nodeC = Node(2, nodeD)
    nodeB = Node(3, nodeC)
    nodeA = Node(4, nodeB)

    deleteNode(nodeB)
    print([nodeA.data, nodeB. data, nodeC.data])

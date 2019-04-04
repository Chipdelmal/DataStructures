# Linked List

## Data Structure Summary

* Data is stored in non contiguous memory locations
* No arbitrary access to data (sequential only)

Useful for: variable lengths, homogeneous data types, queues/stacks

### Complexity

| Action  |  Cost |
|---------|-------|
| Access  | O(n)  |
| Search  | O(n)  |
| Insert (beginning)  | O(1) |
| Insert (end)  | O(n) |

## Class Definition

```python
getHead:
traverseList:
printTraverseList:
addNode:
addTail:
addHead:
```

# Exercises: Linked Lists

1. **Remove Dups***: Write code to remove duplicates from an unsorted linked list.
2. **Return Kth to Last***: Implement an algorithm to find the kth to last element of a singly linked list
3. **Delete Middle Node**: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.
4. **Partition**: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
5. **Sum Lists**: You have two numbers represented by a linked list, where each node contains a single digit.The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
6. **Palindrome**: Implement a function to check if a linked list is a palindrome.
7. **Intersection**: Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is de ned based on reference, not value.That is, if the kth node of the  rst linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
8. **Loop Detection**: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

*McDowell, Gayle Laakmann (2015). Cracking the coding interview : 150 programming questions and solutions. Palo Alto, CA: CareerCup, LLC*

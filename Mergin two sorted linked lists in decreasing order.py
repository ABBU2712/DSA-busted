# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(msg, head):
 
    print(msg, end='')
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Function to merge two sorted lists from the end
def reverseMerge(a, b):
 
    result = None
 
    while a and b:
        if a.data < b.data:
 
            # take the node from the front of the list `a`, and move it
            # to the front of the result
 
            newNode = a
            a = a.next
 
            newNode.next = result
            result = newNode
        else:
            # take the node from the front of the list `b`, and move it
            # to the front of the result
 
            newNode = b
            b = b.next
 
            newNode.next = result
            result = newNode
 
    while b:
        newNode = b
        b = b.next
 
        newNode.next = result
        result = newNode
 
    while a:
        newNode = a
        a = a.next
 
        newNode.next = result
        result = newNode
 
    return result
 
 
if __name__ == '__main__':
 
    a = b = None
 
    for i in reversed(range(2, 6, 2)):
        a = Node(i, a)
 
    for i in reversed(range(1, 10, 2)):
        b = Node(i, b)
 
    # print both lists
    printList('First List: ', a)
    printList('Second List: ', b)
 
    head = reverseMerge(a, b)
    printList('After Merge: ', head)
import sys

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    
    #visited = {}
    if head is None:
        return 0
    
    while 1:
        # if some node points to None then it's not cyclic
        if head.next == None:
            return 0
        
        if hasattr(head, 'id'):  # or by checking the location in memory with id(head) and storing it to a hash
            return 1
        else:
            head.id = 1        
            head = head.next
              
    return 0
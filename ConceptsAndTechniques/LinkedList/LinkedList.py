from typing import Iterator, List, Optional


class SinglyLinkedListNode:
    """
    params:
    - val (int): Integer value of the value of the node
    - nextNode (SinglyLinkedListNode): next node in list
    - vals (List[int]): list of node values, in order (e.g., vals[0] -> vals[1] -> vals[2] ...)
    """
    def __init__(
        self, 
        val: Optional[int] = None, 
        nextNode: Optional["SinglyLinkedListNode"] = None,
        vals: Optional[List[int]] = None # [1,2,5,7,10,3]
    ) -> None:
        if val:
            self.val: int = val
            self.next: Optional["SinglyLinkedListNode"] = nextNode
        elif vals:
            # need to implement this
            prevNode = None
            for v in vals:
                cNode = SinglyLinkedListNode(v, None)
                if prevNode:
                    prevNode.next = cNode
                prevNode = cNode

            self = prevNode
        else:
            raise ValueError("val and nextNode OR vals required, not both.")


    def __iter__(self) -> Iterator["SinglyLinkedListNode"]:
        """
        Returns an iterator for nodes in the singly linked list.
        """
        current = self
        while current is not None:
            yield current
            current = current.next


    def iterValues(self) -> Iterator[int]:
        """
        Returns an iterator for values in the singly linked list.
        """
        current = self
        while current is not None:
            yield current.val
            current = current.next


    def hasNext(self) -> bool:
        "Returns True if there is another node in the list."
        if self.next:
            return True
        else:
            return False
        
    
    def insertAtIndex(self) -> None:
        """
        Inserts a new node at the index. Assume that the index of the head node is 0.
        """
        
        return None


    def addHead(self, node: "SinglyLinkedListNode") -> None:
        """
        Adds a new node as the head node.
        """

        currentHead = SinglyLinkedListNode(self.val, self.next)
        self.val = node.val
        self.next = currentHead

        return None
    

    def removeAtIndex(self, index: int) -> None:
        """
        Remove the node at the index from the list. Assume that the index of the head node is 0.
        """

        idx = 0
        previousNode: Optional[SinglyLinkedListNode] = None
        nodeToRemove: Optional[SinglyLinkedListNode] = None
        for node in self:
            if idx == index:
                # do the remove
                nodeToRemove = node
                # if node.next exists, set node.val = node.next.val, etc.
                # else, set to None
                break

            previousNode = node

        return None
    

    def addTail(self, node: "SinglyLinkedListNode") -> None:
        """
        Adds a new node to the tail of the list. 

        NOTE: This will potentially traverse the entire list to find the tail node.
        """

        for n in self:
            if n.next is None:
                n.next = node
                break

        return None




single: Optional[SinglyLinkedListNode] = SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3, None)))
single: Optional[SinglyLinkedListNode] = SinglyLinkedListNode(vals=[1,2,3,4,5])
currentNode: Optional[SinglyLinkedListNode] = single

while currentNode is not None:
    print(currentNode.val)
    currentNode = currentNode.next

# return nodes
for s in single:
    print(s.val)

# return values of nodes
for s in single.iterValues():
    print(s)


single.addHead(SinglyLinkedListNode(12341234, None))
for s in single.iterValues():
    print(s)


single.addTail(SinglyLinkedListNode(10000000001, None))
for s in single.iterValues():
    print(s)





class SLL:
    def __init__(self, val, nextNode):
        self.val = val
        self.next = nextNode

sll = SLL(1, SLL(2, SLL(3, None)))
currNode = sll

while currNode:
    print(currNode.val)
    currNode = currNode.next
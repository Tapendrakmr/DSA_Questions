# basic format
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def pushElementAtEnd(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode
        return

    def print(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    # Write a Program to reverse the Linked List. (Both Iterative and recursive)
    # Iterative
    def reverseLL(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        print("reverse process is done")


SLL = SingleLL()
SLL.pushElementAtEnd(20)
SLL.pushElementAtEnd(30)
SLL.pushElementAtEnd(40)
SLL.pushElementAtEnd(50)
SLL.print()
SLL.reverseLL()
SLL.print()

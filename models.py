from typing import Optional


class Node:
    def __init__(self, value: Optional[int], previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.data = Node(None)

    def append(self, item: int):
        if self.data.value is None:
            self.data.value = item
        else:
            self.data.previous = self.data
            self.data.value = item
            self.data.next = None

    def remove(self, item):
        current = self.data
        while (current is not None):
            if current.value == item:
                self.data.previous.next = self.data.next
                self.data.value = None
                break
            current = self.data.previous

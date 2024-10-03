
from models import DoublyLinkedList

dll = DoublyLinkedList()
dll.append(3)
dll.append(5)
dll.append(6)
dll.append(7)
dll.remove(6)
print("This is the content of my DoublyLinkedList : {}".format(dll))

from models import DoublyLinkedList


def test_add_first_element_dll():
    dll = DoublyLinkedList()
    dll.append(1)
    #assert dll.len == 1
    assert dll.data.value == 1 and dll.data.previous == None and dll.data.next == None

def test_add_second_element_dll():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    #assert dll.len == 2
    assert dll.data.value == 2 and dll.data.previous != None
    print(dll.data.previous.value)
    assert dll.data.previous.value == 1 and dll.data.next == None

test_add_first_element_dll()
test_add_second_element_dll()

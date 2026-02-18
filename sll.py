#
# Gagnaskipan.
# Single-Linked-List
# Student(s):
#  - Ísak Elí Hauksson
#
from sll_node import Node
from iterator import NodeIterator


class SLList:
    """
    **Methods For Both SLL and DLL**

    - `is_empty()`: Returns True if empty
    - `front()`: Return the first item without removing it.
    - `back()`: Return the last item without removing it.
    - `push_front(item)`: Insert `item` at the front.
    - `push_back(item)`: Insert `item` at the back.
    - `pop_front()`: Remove and return the first item.
    - `pop_back()`: Remove and return the last item.
    """

    def __init__(self):
        """
        Constructor.
        Time complexity: O(1)
        """
        self._head: Node | None = None
        self._tail: Node | None = None
        self._len = 0

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        return NodeIterator(self._head)

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        elems = []
        node = self._head
        while node is not None:
            elems.append(str(node.item))
            node = node.next
        return "[" + ", ".join(elems) + "]"

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        return self._len

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return (
            self._head is None
        )  # could alternatively check _tail is None, or _len is 0.

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError("front called on an empty list")
        return self._head.item

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        if self.is_empty():
            raise IndexError("back called on an empty list")
        return self._tail.item

    def push_front(self, item) -> None:
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        # Create a new node
        new_node: Node = Node(item)

        if self.is_empty():
            self._head, self._tail = new_node, new_node
            return

        new_node.next = self._head
        self._head = new_node
        self._len += 1

    def pop_front(self) -> object:
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: returns the item (because it is 'pop'), but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError("pop_front called on an empty list")

        if self._head == self._tail:  # if n==1
            self._head, self._tail = None, None

        r_value = self._head  # The return value

        self._head = self._head.next if self._head is not None else None

        self._len -= 1
        return r_value

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        # Create A a new node
        new_node: Node = Node(item)

        if self.is_empty():
            self._head, self._tail = new_node, new_node
            return

        self._tail.next = new_node
        self._tail = new_node

        self._len += 1

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(n)
        :return: returns the item (because it is 'pop'), but trows an exception if list empty.
        """
        if self.is_empty():
            raise IndexError("pop_front called on an empty list")

        if self._head == self._tail:  # if n==1
            self._head, self._tail = None, None

        current_node = self._head
        next_node = current_node.next

        # Loop until end is found
        while next_node.next is not None:
            current_node = current_node.next
            next_node = current_node.next

        # Put self tail to the new last node
        self._tail = current_node

        # So the last node points at None
        current_node.next = None

        self._len -= 1
        return next_node

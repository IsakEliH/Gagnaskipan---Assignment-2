#
# Gagnaskipan.
# Double-Linked-List
# Student(s):
#  - Ísak Elí Hauksson
#
from dll_node import Node
from iterator import NodeIterator

class Position:
    __slots__ = ['node']

    def __init__(self, node):
        self.node = node


class DLList:

    #
    # Beginning of fundamental section.
    #

    def __init__(self):
        ...

    def __iter__(self):
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        ...

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        ...
        return ""

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        ...
        return 0

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        ...
        return True

    def get_at(self, pos: Position) -> object:
        """
        Return element at position 'pos'.
        :param pos: Position to insert
        :return: Element
        """
        ...
        return None

    def insert_after(self, pos: Position, item: object) -> Position:
        """
        Insert element following position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        ...

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.
        :param pos: Position to insert
        :param item:Element to insert
        :return: Position of inserted element
        """
        ...

    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.
        :param pos: Position of element to remove.
        :return: Element deleted
        """
        ...
        return None

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.
        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        ...
        return None

    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        ...
        return None

    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        ...
        return None

    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """
        ...
        return None

    def next_pos(self, pos: Position) -> Position | None:
        """
         Return position following 'pos', or None if already at end of list.
         """
        ...
        return None

    #
    # End of fundamental section.
    # Implement the methods below by, for the most part, using/calling the ones you have implemented above.
    # Avoid unnecessary code duplication.
    #

    def front(self):
        """
        Returns the element at the front of the list.
        Time complexity: O(1)
        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        ...
        return None

    def back(self):
        """
        Returns the element at the back of the list.
        Time complexity: O(1)
        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        ...
        return None

    def push_front(self, item):
        """
        Insert an element to front of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        ...

    def pop_front(self):
        """
        Remove an element from the front of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        ...

    def push_back(self, item):
        """
        Insert an element to back of the list.
        Time complexity: O(1)
        :param item: element to insert
        :return: None
        """
        ...

    def pop_back(self):
        """
        Remove an element from the back of the list.
        Time complexity: O(1)
        :return: None, but trows an exception if list empty.
        """
        ...

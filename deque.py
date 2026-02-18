#
# Gagnaskipan.
# Deque implementation
# Student(s):
#  - Ísak Elí Hauksson
#

from sll import SLList
from dll import DLList


class Deque:
    def __init__(self, lst: SLList | DLList):
        """
        Constructor.
        """
        ...

    def __len__(self):
        """
        Returns the number of elements in the deque.
        :return: Number of elements.
        """
        ...
        return 0

    def __str__(self):
        """
        Returns the string representation of the deque.
        :return: String representation.
        """
        ...
        return ""

    def is_empty(self):
        """
        Returns True if the deque is empty, otherwise False.
        """
        ...
        return True

    def front(self):
        """
        Returns the front (left) element of the deque (without removing it).
        :return: If non-empty, the front element, otherwise raises exception.
        """
        ...
        return None

    def back(self):
        """
        Returns the back (right) element of the deque (without removing it).
        :return: If non-empty, the front element, otherwise raises exception.
        """
        ...
        return None

    def append(self, item):
        """
        Inserts the element to the right (back) of the deque.
        :return: None
        """
        ...

    def appendleft(self, item):
        """
        Inserts the element to the left (front) of the deque.
        :return: None
        """
        ...

    def pop(self):
        """
        Removes the element at the right (back) of the deque.
        :return: None. Raises an exception if empty.
        """
        ...

    def popleft(self):
        """
        Removes the element at the left (front) of the deque.
        :return: None. Raises an exception if empty.
        """
        ...

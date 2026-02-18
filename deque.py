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
        self._lst = lst

    def __len__(self):
        """
        Returns the number of elements in the deque.
        :return: Number of elements.
        """
        return len(self._lst)

    def __str__(self):
        """
        Returns the string representation of the deque.
        :return: String representation.
        """
        return str(self._lst)

    def is_empty(self):
        """
        Returns True if the deque is empty, otherwise False.
        """
        return self._lst.is_empty()

    def front(self):
        """
        Returns the front (left) element of the deque (without removing it).
        :return: If non-empty, the front element, otherwise raises exception.
        """
        return self._lst.front()

    def back(self):
        """
        Returns the back (right) element of the deque (without removing it).
        :return: If non-empty, the front element, otherwise raises exception.
        """
        return self._lst.back()

    def append(self, item):
        """
        Inserts the element to the right (back) of the deque.
        :return: None
        """
        self._lst.push_back(item)

    def appendleft(self, item):
        """
        Inserts the element to the left (front) of the deque.
        :return: None
        """
        self._lst.push_front(item)

    def pop(self):
        """
        Removes the element at the right (back) of the deque.
        :return: None. Raises an exception if empty.
        """
        self._lst.pop_back()

    def popleft(self):
        """
        Removes the element at the left (front) of the deque.
        :return: None. Raises an exception if empty.
        """
        self._lst.pop_front()

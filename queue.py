#
# Gagnaskipan.
# Deque implementation
# Student(s):
#  - Ísak Elí Hauksson
#

from sll import SLList
from dll import DLList


class Queue:
    def __init__(self, lst: SLList | DLList):
        """ "
        Constructor.
        """
        ...

    def __len__(self):
        """ "
        Returns the number of elements in the queue.
        """
        ...
        return 0

    def __str__(self):
        """
        Returns the string representation of the queue.
        """
        ...
        return ""

    def is_empty(self):
        """
        Returns True if queue is empty, otherwise False.
        """
        ...
        return True

    def front(self):
        """
        Returns the front element of the queue (without removing it).
        :return: If non-empty, the front element of the queue, otherwise throws exception.
        """
        ...
        return None

    def enqueue(self, item):
        """
        Inserts the element to the back of the queue.
        """
        ...

    def dequeue(self):
        """
        Removes the element at the front of the queue (without returning)..
        """
        ...

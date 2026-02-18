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
        self._lst: SLList | DLList = lst

    def __len__(self):
        """ "
        Returns the number of elements in the queue.
        """
        return len(self._lst)

    def __str__(self):
        """
        Returns the string representation of the queue.
        """
        return str(self._lst)

    def is_empty(self):
        """
        Returns True if queue is empty, otherwise False.
        """
        return self._lst.is_empty()

    def front(self):
        """
        Returns the front element of the queue (without removing it).
        :return: If non-empty, the front element of the queue, otherwise throws exception.
        """
        return self._lst.front()

    def enqueue(self, item):
        """
        Inserts the element to the back of the queue.
        """
        self._lst.push_back(item)

    def dequeue(self):
        """
        Removes the element at the front of the queue (without returning)..
        """
        self._lst.pop_front()

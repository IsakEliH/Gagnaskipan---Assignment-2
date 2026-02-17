#
# Gagnaskipan.
# Stack implementation
# Student(s):
#  - Ísak Elí Hauksson
#
import sll
import dll

class Stack:

    def __init__(self, lst):
        self._lst = lst

    def __len__(self):
        """
        Returns number of elements in the stack.
        :return: Number of elements.
        """
        return len(self._lst)

    def __str__(self):
        """
        Returns a string representation of the stack.
        :return: String representation.
        """
        return str(self._lst)

    def is_empty(self):
        """
        Returns True if the stack is empty.
        :return: True if empty, otherwise false.
        """
        return self._lst.is_empty()

    def top(self):
        """
        Returns the top element of the stack (without removing it).
        :return: Top element
        """
        return self._lst.front()

    def pop(self):
        """
        Removes the top element of the stack.
        :return: None, throws an exception if empty.
        """
        self._lst.pop_front()

    def push(self, item):
        """
        Insert element on top of stack"
        :param item: Element to insert.
        :return:  None
        """
        self._lst.push_front(item)


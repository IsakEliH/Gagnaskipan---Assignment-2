#
# Gagnaskipan.
# Double-Linked-List
# Student(s):
#  - Ísak Elí Hauksson
#
from dll_node import Node
from iterator import NodeIterator


class Position:
    __slots__ = ["node"]

    def __init__(self, node: Node):
        self.node = node


class DLList:
    __slots__ = [
        "sentinel_front",
        "sentinel_back",
        "_size",
    ]

    def __init__(self):
        """
        Create a sentinel node
        """
        self.sentinel_front: Node = Node("SENTINEL_1", sentinel=True)
        self.sentinel_back: Node = Node("SENTINEL_2", sentinel=True)
        self._size = 0

    def __iter__(self) -> NodeIterator:
        """
        Implemented as part of the iterator interface to allow: for ... in A
        :return: Iterator object.
        """
        # TODO: Add Iter method
        ...

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)
        :return: The string representation.
        """
        # TODO: Add better string method

        if self.is_empty():
            return "[]"

        r_string = "["
        current_node = self.sentinel_front.next

        while not current_node.sentinel:
            r_string += str(current_node.item) + ", "
            current_node = current_node.next

        r_string = r_string[:-2] if r_string[-2:] == ", " else r_string
        return r_string + "]"

    def __len__(self):
        """
        Returns the number of elements in the list.
        Time complexity: O(1)
        :return: Number of elements in the list.
        """
        return self._size

    def _starter_node(self, new_node: Node) -> Position:
        """
        Helper function for when adding the first node:
        Makes this node the started node (the first node)
        connected to both ends (sentinels)

        :param new_node: The new starter node
        :type new_node: Node
        :returns: current position
        :rtype: Position
        """

        # Make the sentinel back and front point at the same starting node
        self.sentinel_front.next = new_node
        self.sentinel_front.prev = self.sentinel_back

        self.sentinel_back.prev = new_node
        self.sentinel_back.next = self.sentinel_front

        new_node.prev = self.sentinel_front
        new_node.next = self.sentinel_back
        pos = Position(new_node)

        self._size += 1

        return pos

    def is_empty(self):
        """
        Checks if list is empty.
        Time complexity: O(1)
        :return: True if empty, otherwise false
        """
        return self._size == 0

    def get_at(self, pos: Position) -> object:
        """
        Return element at position 'pos'.
        :param pos: Position to insert
        :return: Element
        """

        return pos.node.item

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
        new_node: Node = Node(item)

        # Add as first node if empty
        if self.is_empty():
            return self._starter_node(new_node)

        new_front_node = pos.node.prev
        new_front_node.next = new_node

        new_node.prev = new_front_node
        new_node.next = pos.node
        pos.node.prev = new_node

        new_pos = Position(new_node)

        self._size += 1

        return new_pos

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


array = DLList()
print(array)
s_pos = Position(Node(None))
for i in range(10):
    s_pos = array.insert_before(s_pos, i)
    print(array)
    print(array.get_at(s_pos))

print(array)

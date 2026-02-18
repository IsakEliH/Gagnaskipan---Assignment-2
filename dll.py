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

        # Wire sentinels to avoid edge cases
        self.sentinel_front.next = self.sentinel_back
        self.sentinel_front.prev = self.sentinel_back
        self.sentinel_back.prev = self.sentinel_front
        self.sentinel_back.next = self.sentinel_front

    def __iter__(self) -> NodeIterator:
        """
        Implemented as part of the iterator interface to allow: for ... in A

        :return: Iterator object.
        """
        return NodeIterator(self.sentinel_front.next, self.sentinel_back)

    def __str__(self):
        """
        String representation of the list.
        Time complexity: O(n)

        :return: The string representation.
        """
        return "[" + ", ".join(str(x) for x in self) + "]"

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
        self.sentinel_front.next = new_node
        self.sentinel_back.prev = new_node

        new_node.prev = self.sentinel_front
        new_node.next = self.sentinel_back

        self._size += 1
        return Position(new_node)

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

        :raises IndexError: Invalid position
        :param pos: Position to insert
        :param item: Element to insert
        :return: Position of inserted element
        """
        if (
            pos is None
            or pos.node is None
            or pos.node.next is None
            or pos.node.prev is None
        ):
            raise IndexError("Invalid position")

        new_node: Node = Node(item)

        # Add as first node if empty
        if self.is_empty():
            return self._starter_node(new_node)

        new_back_node = pos.node.next
        new_back_node.prev = new_node

        # Connect new node
        new_node.next = new_back_node
        new_node.prev = pos.node
        pos.node.next = new_node

        self._size += 1

        return Position(new_node)

    def insert_before(self, pos: Position, item: object) -> Position:
        """
        Insert element before position 'pos' in the list.

        :raises IndexError: Invalid position
        :param pos: Position to insert
        :param item: Element to insert
        :return: Position of inserted element
        """
        if (
            pos is None
            or pos.node is None
            or pos.node.next is None
            or pos.node.prev is None
        ):
            raise IndexError("Invalid position")

        new_node: Node = Node(item)

        # Add as first node if empty
        if self.is_empty():
            return self._starter_node(new_node)

        new_front_node = pos.node.prev
        new_front_node.next = new_node

        new_node.prev = new_front_node
        new_node.next = pos.node
        pos.node.prev = new_node

        self._size += 1

        return Position(new_node)

    def remove(self, pos: Position) -> object:
        """
        Remove element at position 'pos' in the list.

        :param pos: Position of element to remove.
        :return: Element deleted
        """
        if pos is None or pos.node is None or pos.node.sentinel:
            raise IndexError("Cannot remove sentinel / invalid position")

        return_item = pos.node.item

        pos.node.prev.next = pos.node.next
        pos.node.next.prev = pos.node.prev

        pos.node.next, pos.node.prev = None, None

        self._size -= 1

        return return_item

    def replace(self, pos: Position, item: object) -> object:
        """
        Replace element at position 'pos' in the list.

        :param pos: Position of element to replace
        :param item: New element to replace the existing one.
        :return: The element replaced (formerly at position)
        """
        existing_item = pos.node.item
        pos.node.item = item
        return existing_item

    def front_pos(self) -> Position | None:
        """
        Return position of the element at the head of the list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return None
        return Position(self.sentinel_front.next)

    def back_pos(self) -> Position | None:
        """
        Return position of the element at the end of list if list non-empty, or None if list is empty.
        """
        if self.is_empty():
            return None
        return Position(self.sentinel_back.prev)

    def prev_pos(self, pos: Position) -> Position | None:
        """
        Return position before 'pos', or None if already at front of list.
        """

        if pos.node.prev.sentinel:
            return None
        return Position(pos.node.prev)

    def next_pos(self, pos: Position) -> Position | None:
        """
        Return position following 'pos', or None if already at end of list.
        """
        if pos.node.next.sentinel:
            return None
        return Position(pos.node.next)

    #
    # End of fundamental section.
    # Implement the methods below by, for the most part, using/calling the ones you have implemented above.
    # Avoid unnecessary code duplication.
    #

    def _get_endpoint(self, endpoint: str = "front") -> Position:
        """
        Helper function to reduce code duplication.
        Returns the position of the front or back of the list.
        raises error when list is empty.

        :param endpoint: Should only be "front" or "back". If not make "front"
        :raises IndexError: When the list is empty
        :return: The position of the front or back
        :rtype: Position
        """

        # To make sure that KeyError does not show up
        if endpoint not in ("front", "back"):
            endpoint = "front"

        front_back: dict = {"front": self.front_pos(), "back": self.back_pos()}

        pos: Position | None = front_back[endpoint]

        if pos is None:
            raise IndexError("The list is empty")

        return pos

    def front(self) -> object:
        """
        Returns the element at the front of the list.
        Time complexity: O(1)

        :return: If list non-empty, the front element, otherwise trows an exception.
        """
        pos: Position = self._get_endpoint("front")

        return pos.node.item

    def back(self) -> object:
        """
        Returns the element at the back of the list.
        Time complexity: O(1)

        :return: If list non-empty, the back element, otherwise trows an exception.
        """
        pos: Position = self._get_endpoint("back")

        return pos.node.item

    def push_front(self, item) -> None:
        """
        Insert an element to front of the list.
        Time complexity: O(1)

        :param item: element to insert
        :return: None
        """
        # Insert right after the front sentinel
        self.insert_after(Position(self.sentinel_front), item)

    def pop_front(self) -> object:
        """
        Remove an element from the front of the list.
        Time complexity: O(1)

        :return: returns the item (because it is 'pop'), but trows an exception if list empty.
        :rtype: object
        """
        pos: Position = self._get_endpoint("front")

        item = self.remove(pos)

        return item

    def push_back(self, item) -> None:
        """
        Insert an element to back of the list.
        Time complexity: O(1)

        :param item: element to insert
        :return: None
        """
        self.insert_before(Position(self.sentinel_back), item)

    def pop_back(self) -> object:
        """
        Remove an element from the back of the list.
        Time complexity: O(1)

        :return: returns the item (because it is 'pop'), but trows an exception if list empty.
        :rtype: object
        """
        pos: Position = self._get_endpoint("back")

        item = self.remove(pos)

        return item

class Node:
    # Optimization (can omit) to tell Python to use a more
    # compact data structure to represent its class member
    # variables (uses dict by default, but now uses a fixed-size
    # array!). You see, knowing data-structures IS IMPORTANT!
    __slots__ = ["prev", "item", "next", "sentinel"]

    def __init__(self, item, next=None, prev=None, sentinel=False):
        self.item: object = item
        self.next: Node | None = next
        self.prev: Node | None = prev
        self.sentinel: bool = sentinel

class Node:
    # Optimization (can omit) to tell Python to use a more
    # compact data structure to represent its class member
    # variables (uses dict by default, but now uses a fixed-size
    # array!). You see, knowing data-structures IS IMPORTANT!
    __slots__ = ['item', 'next']

    def __init__(self, item, next= None) -> None:
        self.item = item
        self.next = next

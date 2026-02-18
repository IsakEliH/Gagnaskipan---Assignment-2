class NodeIterator:
    def __init__(self, node, node_end=None):
        self.__node = node
        self.__node_end = node_end

    def __iter__(self):
        return self

    def __next__(self):
        if self.__node is None or self.__node is self.__node_end:
            raise StopIteration
        item = self.__node.item
        self.__node = self.__node.next
        return item

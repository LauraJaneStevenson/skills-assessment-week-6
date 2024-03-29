"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def get_nodes(self, data):
        """ Return a list of nodes with the given data

        For example::

            >>> b1 = Node("B")
            >>> b2 = Node("B")
            >>> e = Node("E")
            >>> c = Node("C", [ b1, e])
            >>> a = Node("A", [b2, c])
            >>> tree = Tree(a)
            >>> result = tree.get_nodes("B")
            >>> result == [b2, b1]
            True
            >>> tree.get_nodes("L")
            []

        """

        # list of nodes to return
        r_lst = []

        # create list of nodes to visit
        to_visit = [self.root]

        # loop through to visit list
        while to_visit:

            # get current node from begining 
            current = to_visit.pop(0)
            # check current node's data matches what we're look for
            if current.data == data:
                # add current node to return list
                r_lst.append(current)

            # set to visit list to current node's children
            to_visit.extend(current.children)

        return r_lst


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()

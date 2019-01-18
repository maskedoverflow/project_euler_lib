import itertools


class Tree:

    def __init__(self, value, children):
        self.value = value
        self._children = list(children)

    def __getitem__(self, item):
        return self._children[item]

    def __setitem__(self, key, value):
        self._children[key] = value

    def __iter__(self):
        return iter(self._children)

    def __len__(self):
        return len(self._children)

    def __str__(self):
        return f"({self.value}, {', '.join(str(child) for child in self) if any(self) else '()'})"


class BinaryTree(Tree):

    def __init__(self, value, left, right):
        super().__init__(value, (left, right))

    @property
    def left(self):
        return self[0]

    @left.setter
    def left(self, tree):
        self[0] = tree

    @property
    def right(self):
        return self[1]

    @right.setter
    def right(self, tree):
        self[1] = tree

    def add_to_bottom(self, values):
        if not any(child for child in self):
            self.left = next(values)
            self.right = next(values)
        else:
            for child in self:
                child.add_to_bottom(values)

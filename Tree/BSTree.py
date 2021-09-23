class BSTree:

    def __init__(self, data=None, subleft=None, subright=None):
        """
        :param data: the data stored in this root
        :param subleft: the left child of the tree
        :param subright: the right child of the tree
        """
        self.data = data
        self.subleft = subleft
        self.subright = subright

    def add(self, newdata):
        """
        add a new element into the tree
        :param newdata: the element
        :return: None
        """
        # if this data in the tree and it is exactly the tree we are looking at
        if newdata == self.data:
            return
        # if the tree in None, then store the data here
        if self.data is None:
            self.data = newdata

        # comparing the hash value of self.data and new data
        # if hash value of newdata is smaller, than add it to subleft
        # else add it to subright, this is a recursion fuction
        if hash(self.data) > hash((newdata)):
            # if the left child tree doesn't exist yet, we need to create one first
            if not self.subleft:
                self.subleft = BSTree()
            return self.subleft.add(newdata)
        else:
            if not self.subright:
                self.subright = BSTree()
            return self.subright.add(newdata)

    def add_tree(self, newtree):
        """
        This function will merge a tree into our tree
        :param newtree: the new tree
        :return: None
        """
        if newtree and newtree.data:
            self.add(newtree.data)
            self.add_tree(newtree.subleft)
            self.add_tree(newtree.subright)

    def find(self, data):
        """
        This function will find which part of tree stored the data and return the tree
        :param data: target data
        :return: the tree which self.data is data
        """
        # if the data is None, return None
        if not data:
            return None

        # if this tree contains the data, return the tree
        if data == self.data:
            return self

        # comparing hash value determine which child tree we need to check
        if hash(data) < hash(self.data):
            # if the tree doesn't exist, return None
            if not self.subleft:
                return None
            return self.subleft.find(data)
        else:
            if not self.subright:
                return None
            return self.subright.find(data)

    def remove_data(self, data):
        """
        This method will remove a subtree from the tree by setting all its attribution to None
        :param data: the data of the target tree
        :return: None
        """
        # if the data is None, then end the method
        if not data:
            return
        # find the tree, end when doesn't exist
        the_tree = self.find(data)
        if not the_tree:
            return
        # record child trees
        tree_l = the_tree.subleft
        tree_r = the_tree.subright

        # remove
        the_tree.data = None
        the_tree.subright = None
        the_tree.subleft = None

        # merge the child trees
        self.add_tree(tree_l)
        self.add_tree(tree_r)
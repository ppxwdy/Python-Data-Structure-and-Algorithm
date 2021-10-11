class fbt:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def bfs(self, node, record=None):
        pass

    def add_data(self, data):
        """
        add data to the tree, from left to right
        :param data: the data
        :return: None
        """
        if not self.data:
            self.data = data
            return

        # if not self.left:
        #     self.left = fbt(data)
        #
        # if not self.right:
        #     self.right = fbt(data)
        pass

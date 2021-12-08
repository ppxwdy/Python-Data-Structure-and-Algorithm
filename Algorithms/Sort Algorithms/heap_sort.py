class Heap():

    def __init__(self, arr):
        self.heap = arr
        self.length = len(arr)
        self.build_max_heap()

    def left(self, idx):
        print(1)
        """
        
        find left child node
        :param idx: idx of father
        :return: idx of child
        """


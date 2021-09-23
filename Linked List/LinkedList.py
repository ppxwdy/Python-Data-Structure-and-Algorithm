class ListNode:

    def __init__(self, val, nex=None):
        self.val = val
        self.nex = nex


class LinkedList:

    def __init__(self, head=None, tail=None, length=0):
        """
        The linked list have three attributes
        :param head: the first node of the list
        :param tail: the last node of the list
        :param length: the number of node in the list
        """
        self.head = head
        self.tail = tail
        self.length  = length

    def add(self, val):
        """
        This method add a new data to the list, which means create a new node and add to the tail
        which makes the new node the new tail.
        :param val: the data
        :return: None
        """

        new_tail = ListNode(val)
        # if this is a new list
        if not self.head:
            self.head = new_tail
            self.tail = new_tail
        # otherwise
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        self.length += 1

    def pop(self, index=None):
        """
        The function like the list.pop(), it will remove the node
        from the list and return it to you
        :param index: the index of the node in the list
        :return: the node
        """
        the_node = None

        # if the index larger than the length, then the order is wrong
        # stop the method by raising a error
        if index and index >= self.length:
            raise ValueError('index out of range')

        # for the default index, pop the tail
        if not index:
            index = self.length - 1

        predecessor = None     # the node before the current node
        cur = self.head        # the node we are looking at
        count = 0              # count the time
        while count < self.length:
            if count == index:          # if we get to the given point
                the_node = cur          # cur will be our return node
                successor = cur.nex     # find the node after cur
                predecessor.nex = successor     # link suc to pre, then it will change p-c-s to p-s
                self.length -= 1        # losing one node, length minus 1

                if index == 0:          # if pop head, get a new head
                    self.head = successor

                if index == self.length -1:  # if pop tail, then find a new tail
                    self.tail = predecessor
                break                   # end the loop
            count += 1
            predecessor = cur           # for the next checking, the new pre will be the cur for this time
            cur = cur.nex               # cur will be cur next


        return the_node

    def __get_node(self, start, index):
        """
         find the requried node, this is a operation on node
         it is a private method for the get() function use only
        :param start: the start node
        :param index: the index of the node in the list
        :return: the node
        """
        if index and index > self.length:
            raise ValueError('index out of range')

        if index == 0:
            return self.head
        else:
            return self.__get_node(start.nex, index-1)

    def get(self, index):
        """
        this method will use the __get_node find the node and return its val
        :param index: the index of the node in the list
        :return:
        """
        return self.__get_node(self.head, index).val

    def reverse(self):
        """
        this function will reverse the linked list in place
        :return: None
        """
        if not self.head:
            return

        old_head = self.head  # record the old head

        pre_node = None       # the node before current node
        cur_node = self.head   # current node
        while cur_node:         # when cur_node is not None
            # start swap relation
            temp = cur_node.nex
            cur_node.nex = pre_node
            pre_node = cur_node
            cur_node = temp

            # new head is the old tail which is pre in this situation
            # new tail is the old head
            self.head, self.tail = self.tail, self.head
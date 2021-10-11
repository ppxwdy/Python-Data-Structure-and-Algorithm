class sorts:

    def __init__(self, original_list):
        self.original_list = original_list

    def insertion_sort(self, find_min=False, reverse=False):
        """
        Insertion sort, could be used to find the min value of the data
        :param reverse: True return max to min else min to max
        :param find_min: True return min value, otherwise just sort
        :return: min value or none
        """

        # from the last element, the target val, compare it with the element before it
        for i in range(len(self.original_list)-1, -1, -1):
            # compare the element with the element before the target
            for j in range(i-1, -1, -1):
                # if target smaller, switch
                if self.original_list[i] <= self.original_list[j]:
                    self.original_list[i], self.original_list[j] = self.original_list[j], self.original_list[i]
                    # if we need to find the min and the min has been found
                    if find_min and j == 0:
                        # return the min value
                        return self.original_list[0]
                else:
                    # no element smaller, stop the loop
                    break
        if reverse:
            self.original_list = self.original_list[::-1]

    def bubble_sort(self, find_max=False, reverse=False):
        """
        Bubble sort, could be used to find the max value of the data
        :param reverse: True return max to min else min to max
        :param find_max: True return max value, otherwise just sort
        :return: max value or none
        """

        # from the first element, the target val, compare it with the element behind it
        for i in range(len(self.original_list)):
            # compare the element with the element behind the target
            for j in range(i + 1, len(self.original_list)):
                # if target larger, switch
                if self.original_list[i] >= self.original_list[j]:
                    self.original_list[i], self.original_list[j] = self.original_list[j], self.original_list[i]
                # if we need to find the max and the max has been found
                if find_max and j == 0:
                    # return the maxvalue
                    return self.original_list[-1]
        if reverse:
            self.original_list = self.original_list[::-1]

    def quick_sort(self, target=None, key=True, reverse=False):
        """
        Quick_sort
        :param reverse: True return max to min else min to max
        :param key: if we have not assigned the original list to the method, then True
        :type target: the target list
        :return: sorted list
        """

        # the first time, set the original list as the target list
        if key:
            target = self.original_list
        length = len(target)
        if length <= 1:
            return target

        # set the middle element as the pivot
        pivot = target[length // 2]

        # left is the val <= pivot
        left = [num for num in target[:length//2]+target[1+length//2:] if num <= pivot]
        # right is the val > pivot

        right = [num for num in target[:length//2]+target[1+length//2:] if num > pivot]

        # sort left
        # sort right
        # the target after sorting
        sorted_l = sorts(left)
        sorted_r = sorts(right)
        rtn = sorted_l.quick_sort(left, False) + [pivot] + sorted_r.quick_sort(right, False)

        if reverse and key:
            rtn = rtn[::-1]
        return rtn

    def merge_sort(self, target=None, key=True, reverse=False):
        """
        Merge sort.
        :param reverse: True return max to min else min to max
        :param key: if we have not assigned the original list to the method, then True
        :type target: the target list
        :return: None
        """
        # the first time, set the original list as the target list
        if key:
            target = self.original_list
        length = len(target)
        if length <= 1:
            return target

        # split it from middle
        left = target[:length//2]
        right = target[length//2:]

        sorted_l = sorts(left)
        sorted_r = sorts(right)

        left = sorted_l.merge_sort(left, False)
        right = sorted_r.merge_sort(right, False)

        sortedlist = []

        # index for n1, n2
        n1 = 0
        n2 = 0
        # merge two list
        while n1 < length//2 and n2 < length - length//2:
            if left[n1] <= right[n2]:
                sortedlist.append(left[n1])
                n1 += 1
            else:
                sortedlist.append(right[n2])
                n2 += 1

        # append the list which not used up to the end of sorted list
        sortedlist += left[n1:] if n1 < length//2 else right[n2:]

        if reverse:
            sortedlist = sortedlist[::-1]

        return sortedlist

    def counting_sort(self):
        """
        counting sort
        :return: the sorted list
        """

        # create a dict to record the nums and the list of this num
        record = dict()

        # counting
        for n in self.original_list:
            if n in record:
                record[n].append(n)
            else:
                record[n] = [n]

        # applying quick sort to the key list, which has all the distinct num in the original list
        sort = sorts(list(record.keys()))
        nums = sort.quick_sort()
        rtn = []

        # connect the num lists by the order of their values
        for num in nums:
            rtn += record[num]

        return rtn


# l = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3]
# sort = sorts(l)
# # a = sort.counting_sort()
# a = sort.merge_sort()
# print(a)
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        fl = arr[0]
        sl = float('-inf')
        for num in arr:
            if num > fl:
                sl = fl
                fl = num
            elif num > sl and num < fl:
                sl = num
        if sl == float('-inf'):
            return -1
        return sl
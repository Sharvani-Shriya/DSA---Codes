class Solution:
    def secondLargestElement(self, nums):
        largest = nums[0]
        sLargestEle = -1
        n = len(nums)

        for i in range(1,n):
            if nums[i] > largest:
                sLargestEle = largest 
                largest = nums[i]
            elif nums[i] < largest and nums[i] > sLargestEle:
                sLargestEle = nums[i]
        if sLargestEle != -1:
            return sLargestEle
        return -1
                
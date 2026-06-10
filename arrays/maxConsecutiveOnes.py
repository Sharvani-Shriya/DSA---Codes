from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = maxnum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                maxnum = max(cnt, maxnum)
            elif nums[i] == 0:
                cnt = 0
        return maxnum 

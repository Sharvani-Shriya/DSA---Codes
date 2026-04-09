class Solution:
    def twoSum(self, arr, target):
        # code here
        hashmap = {}
        for i,num in enumerate(arr):
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp],i]
            hashmap[num] = i
            
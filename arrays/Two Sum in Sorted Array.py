class Solution:
    def twoSum(self, arr, target):
        #code here
        i,j = 0,len(arr)-1
        while i < j:
            if arr[i] + arr[j] == target:
                return [i+1,j+1]
            elif arr[i] + arr[j] < target:
                i += 1
            else:
                j -= 1
        return [-1,-1]
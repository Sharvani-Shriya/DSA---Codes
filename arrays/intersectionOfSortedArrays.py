class Solution:
    def intersection(self, arr1, arr2):
        #code here
        n1, n2 = len(arr1), len(arr2)
        i = j = 0
        interArr = []
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                i+=1
            elif arr2[j] < arr1[i]:
                j+=1
            else:
                if not interArr or interArr[-1] != arr1[i]:
                    interArr.append(arr1[i])
                i += 1
                j += 1
        return interArr

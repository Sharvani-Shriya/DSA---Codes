class Solution:
    def removeDuplicates(self, arr):
        if not arr:
            return []

        j = 0  # index of last unique element

        for i in range(1, len(arr)):
            if arr[i] != arr[j]:  #We move the pointer j only when we find a new unique element
                j += 1
                arr[j] = arr[i]

        return arr[:j + 1] # Return the array up to the last unique element index + 1 (since j is 0-based)
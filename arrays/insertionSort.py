class Solution:
    def insertionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(1,n):
            j = i
            while arr[j-1] > arr[j] and j > 0:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                j -= 1
            
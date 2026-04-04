class Solution:
    def leftRotate(self, arr, d):
        # code here
        d = d % len(arr)
        arr[:d] = arr[:d][::-1]
        arr[d:] = arr[d:][::-1]
        arr.reverse()
        return arr
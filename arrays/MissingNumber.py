class Solution:
    def missingNum(self, arr):
        # code here
        exor1, exor2 = 0,0
        n = len(arr) 
        for i in range(n):
            exor2 = exor2 ^ arr[i]
            exor1 = exor1 ^ (i + 1)
            
        exor1 = exor1 ^ (n+1)
        return exor1 ^ exor2
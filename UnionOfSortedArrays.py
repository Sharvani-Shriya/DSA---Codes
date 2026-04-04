class Solution:
    def findUnion(self, a, b):
        # code here 
        n1 = len(a)
        n2 = len(b)
        i,j = 0,0
        unionArr = []
        
        while(i < n1 and j < n2):
            if a[i] <= b[j]:
                if len(unionArr) == 0 or unionArr[-1] != a[i]:
                    unionArr.append(a[i])
                i += 1
            else:
                if len(unionArr) == 0 or unionArr[-1] != b[j]:
                    unionArr.append(b[j])
                j += 1
    
        while i < n1:
            if len(unionArr) == 0 or unionArr[-1] != a[i]:
                unionArr.append(a[i])
            i += 1
        
        while j < n2:
            if len(unionArr) == 0 or unionArr[-1] != b[j]:
                unionArr.append(b[j])
            j += 1
        return unionArr
            
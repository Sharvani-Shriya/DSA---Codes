class Solution:
 
    def mergeSort(self, arr, l, r):
        if l >= r:
            return
        mid = (l + r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
    
    def merge(self, arr, low, mid, high):
        temp = []
        l, r = low, mid+1
        while l <= mid and r <= high:
            if arr[l] <= arr[r]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[r])
                r += 1
        if l <= mid:
            temp.extend(arr[l:mid+1])
        elif r <= high:
            temp.extend(arr[r:high+1])
        for i in range(len(temp)):
            arr[low+i] = temp[i]
            
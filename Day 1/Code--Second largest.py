class Solution:
    def getSecondLargest(self, arr):
        max_num=arr[0]
        
        n=len(arr)
        for i in range(0,n):
            if arr[i]>max_num:
                max_num=arr[i]
                
        total_max=arr.count(max_num)
        for k in range(0,total_max):
            arr.remove(max_num)
            
        if len(arr)<=0:
            return -1
            
        second_max_num=arr[0]
        
        m=len(arr)
        for j in range(0,m):
            if arr[j]>second_max_num:
                second_max_num=arr[j]
                
        return second_max_num

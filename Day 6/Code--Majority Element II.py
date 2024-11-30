class Solution:
    # Function to find the majority elements in the array
    def findMajority(arr):
        #Your Code goes here.
        arr_set=set(arr)
        n=len(arr)/3
        new_arr=[]
        for i in arr_set:
            if arr.count(i)>n:
                new_arr.append(i)
                
        new_arr.sort()
        return new_arr
    
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
print(Solution.findMajority(arr))

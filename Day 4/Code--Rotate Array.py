class Solution:
    def rotateArr(arr, d):
        #Your code here
        n = len(arr)
        d %= n
        # rotate first part of array upto d value
        reverse(arr, 0, d-1)
        # rotate second part of array from d to last value
        reverse(arr, d, n-1)
        # rotate whole array
        reverse(arr, 0, n-1)
        return arr

def reverse(arr, SI, EI):
    while SI < EI:
        arr[SI], arr[EI] = arr[EI], arr[SI]
        SI += 1
        EI -= 1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3
print(Solution.rotateArr(arr, d))

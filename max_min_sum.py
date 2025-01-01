def minMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))
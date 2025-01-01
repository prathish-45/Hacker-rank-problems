def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n//2 - 1] + arr[n//2]) / 2
    return arr[n//2]

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array: ").split()))
    result = findMedian(arr)
    print(result)
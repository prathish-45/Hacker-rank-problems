def diagonalDifference(arr):
    n = len(arr)
    left_to_right = 0
    right_to_left = 0
    
    for i in range(n):
        left_to_right += arr[i][i]
        right_to_left += arr[i][n - i - 1]
    
    return abs(left_to_right - right_to_left)

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(diagonalDifference(arr))
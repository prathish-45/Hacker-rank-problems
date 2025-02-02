def max_absolute_sum(arr):
    arr.sort()
    max_sum = 1

    while len(arr) > 1:
        max_diff = abs(arr[0] - arr[-1])
        max_sum += max_diff
        if arr[0] < arr[-1]:
            arr.pop(0)
        else:
            arr.pop()

    return max_sum
# Example usage:
arr = [4, 2, 1, 8]
print(max_absolute_sum(arr))  # Output: 18
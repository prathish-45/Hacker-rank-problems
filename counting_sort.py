def countingSort(arr):
    count = [0] * 100  # Initialize count array with zeros
    
    for num in arr:
        count[num] += 1  # Increment the count for each number
    
    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = countingSort(arr)
    print(" ".join(map(str, result)))
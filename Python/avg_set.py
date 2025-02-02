def average(array):
    size = len(set(array))
    sum = 0
    set_array = set(array)
    for i in set_array:
        sum += i
    return sum/size

if __name__ == '__main__':
    arr = list(map(int, input("Enter the array: ").split()))
    result = average(arr)
    print(result)
    

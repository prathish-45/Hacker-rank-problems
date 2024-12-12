def plusMinus(arr):

    if not arr:
        print("Array is empty")
        return
    postive_count = 0
    negative_count = 0
    zero_count = 0
    
    for i in arr:
        if i > 0:
            postive_count += 1
        elif i < 0:
            negative_count += 1
        elif i == 0:
            zero_count += 1
            
    total_count = len(arr)
    result_positive = postive_count / total_count
    result_negative = negative_count / total_count
    result_zero = zero_count / total_count
    print("{:.6f}".format(result_positive))
    print("{:.6f}".format(result_negative))
    print("{:.6f}".format(result_zero))


arr = [1, 1, 0, -1, -2]
plusMinus(arr)

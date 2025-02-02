#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'filledOrders' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY order
#  2. INTEGER k
#

def filledOrders(order, k):
    # Sort the orders in ascending order
    order.sort()
    
    count = 0
    for o in order:
        if k >= o:
            k -= o
            count += 1
        else:
            break
            
    return count

# Sample Input
order = [5, 4, 6]
k = 3

# Output the result
print(filledOrders(order, k))  # Expected Output: 2


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     order_count = int(input().strip())

#     order = []

#     for _ in range(order_count):
#         order_item = int(input().strip())
#         order.append(order_item)

#     k = int(input().strip())

#     result = filledOrders(order, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()

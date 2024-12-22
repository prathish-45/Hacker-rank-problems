# from itertools import product
# A = [1, 2]
# B = [3, 4]
# print(" ".join(list(map(str, product(A, B)))))

from itertools import product
def iter_tool(A, B):
    lis = list(product(A, B))
    for i in range(len(lis)):
        print(lis[i], end=" ")
"""
input:
1 2
3 4
 
"""       
if __name__ == "__main__":
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    iter_tool(A, B)
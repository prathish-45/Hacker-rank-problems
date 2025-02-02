def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0
    
    for i in range(n):
        for j in range(n):
            # Consider the four possible values for each position in the n x n submatrix
            max_sum += max(matrix[i][j], matrix[i][2*n - j - 1], matrix[2*n - i - 1][j], matrix[2*n - i - 1][2*n - j - 1])
    
    return max_sum

if __name__ == "__main__":
    q = int(input().strip())
    for _ in range(q):
        n = int(input().strip())
        matrix = []
        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))
        result = flippingMatrix(matrix)
        print(result)
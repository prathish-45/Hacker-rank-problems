# if __name__ == "__main__":
#     N, M = map(int, input().split())
#     for i in range(1, N, 2):
#         print((".|." * i).center(M, "-"))
#     print("WELCOME".center(M, "-"))
#     for i in range(N-2, 0, -2):
#         print((".|." * i).center(M, "-"))

def doorMat(N, M):
    for i in range(1, N, 2):
        print((".|." * i).center(M, "-"))
    print(("WELCOME").center(M, "-"))
    for i in range(N-2, 0, -2):
        print((".|." * i).center(M, "-"))
        
if __name__ == "__main__":
    N, M = map(int, input().split())
    doorMat(N, M)
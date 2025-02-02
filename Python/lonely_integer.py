def lonelyInteger(a):
    result = 0
    for num in a:
        result ^= num
    return result

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(lonelyInteger(a))
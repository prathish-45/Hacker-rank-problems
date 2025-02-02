n = int(input())
# Convert to integers instead of strings
t = tuple(map(int, input().split()))
print(hash(t))
from collections import defaultdict

def default_dict(n, m):
    # Initialize defaultdict to store positions
    d = defaultdict(list)
    
    # Process Group A words
    for i in range(n):
        word = input()
        d[word].append(i + 1)
        # print(d)
    
    # Process Group B words
    for _ in range(m):
        word = input()
        # Print positions if word exists, otherwise print -1
        print(*d[word] if d[word] else [-1])
        print(d)

if __name__ == "__main__":
    n, m = map(int, input().split())
    default_dict(n, m)

        
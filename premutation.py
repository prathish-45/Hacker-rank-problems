from itertools import permutations

def itertoolPermutation(s, length):
    result = list(permutations(s, length))
    for i in result:
        print(''.join(i))
    
if __name__ == "__main__":
    s, l = map(str, input().split())
    string = ''.join(sorted(s))
    itertoolPermutation(string, int(l))
    
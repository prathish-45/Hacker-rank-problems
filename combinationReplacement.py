from itertools import combinations_with_replacement

def itertoolPermutation(s, length):
    result = list(combinations_with_replacement(s, length))
    for i in result:
        print(''.join(i))
    
if __name__ == "__main__":
    s, l = map(str, input().split())
    string = ''.join(sorted(s))
    itertoolPermutation(string, int(l))
    
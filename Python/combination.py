from itertools import combinations

def itertoolCombination(string, length):
    for i in range(1, length + 1):
        for j in string:
            result = list(combinations(string, i))
        for k in result:
            print(''.join(k))
    # for i in string:
    #     result = list(combinations(string, length))
    # for i in range(len(result)):
    #     for j in range(len(result)):
            
            
if __name__ == "__main__":
    s, l = map(str, input().split())
    string = ''.join(sorted(s))
    itertoolCombination(string, int(l))
    
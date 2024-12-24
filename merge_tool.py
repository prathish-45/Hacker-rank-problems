# def merge_the_tools(string, k):
#     # your code goes here
#     for i in range(0, len(string), k):
#         s = string[i:i+k]
#         t = ''
#         for c in s:
#             if c not in t:
#                 t += c
#         print(t)

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        s = string[i:i+k]
        # print(s)
        t = ''
        for c in s:
            if c not in t:
                t += c
        print(t)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
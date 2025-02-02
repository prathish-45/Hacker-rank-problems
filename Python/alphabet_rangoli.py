a = chr(97)
print(a * 5)


""" 
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""


def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    n = size
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        print(s)
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
        print(L)
    print('\n'.join(L[:0:-1] + L))
    
if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
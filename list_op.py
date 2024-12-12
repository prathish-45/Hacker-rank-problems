""" 
sample input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""
if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        choice = input()
        stored_inp = choice.split(" ")
        if stored_inp[0] == "insert":
            L.insert(int(stored_inp[1]), int(stored_inp[2]))
        elif stored_inp[0] == "print":
            print(L)
        elif stored_inp[0] == "remove":
            L.remove(int(stored_inp[1]))
        elif stored_inp[0] == "append":
            L.append(int(stored_inp[1]))
        elif stored_inp[0] == "sort":
            L.sort()
        elif stored_inp[0] == "pop":
            L.pop()
        elif stored_inp[0] == "reverse":
            L.reverse()
        
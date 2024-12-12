""" N = int(input())
n = input()
L = []
tuples = n.split(" ")
for i in tuples:
    L.append(int(i))

L = tuple(L)
print(hash(L))

t1 = (1, 2)
print(abs(hash(t1))) """

if __name__ == '__main__':
    n = int(input())  # Read the number of elements
    t = tuple(map(int, input().split()))  # Read the space-separated integers and create a tuple
    print(hash(t))  # Print the hash of the tuple

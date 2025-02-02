from collections import Counter

""" my_list = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print (Counter(my_list))
print(Counter(my_list).items())
print(Counter(my_list).keys())
print(Counter(my_list).values()) """

# n =10 number of shoes
# size = 2 3 4 5 6 8 7 6 5 18 size of 10 shoes
# customers = 6 no. of customers
""" 6 55
6 45
6 55
4 40
18 60
10 50 customers paid amound """
# output = 200 once the size entered total not calculate

""" def shoe_counter(n, size, customers):
    cash = []
    total = 0
    cash = (tuple(map(int, input().split())) for i in range(customers))
    for i in Counter(cash).keys():
        if i[0] in size:
            total += i[1]
        
    print(total)
            
    

if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))
    c = int(input())
    shoe_counter(n, s, c)
 """
# from collections import Counter

def shoe_counter(n, size, customers):
    # Count available shoe sizes
    shoe_inventory = Counter(size)
    print(shoe_inventory)
    total = 0
    
    for _ in range(customers):
        size, price = map(int, input().split())
        # print(shoe_inventory[size])
        if shoe_inventory[size] > 0:
            total += price
            shoe_inventory[size] -= 1
            # print(shoe_inventory[size])
    
    print(total)

if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))
    c = int(input())
    shoe_counter(n, s, c)
    
my_list = [1, 3, 3, 4, 2, 5, 7, 2, 8, 2]
print(Counter(my_list).items())
def swap_case(s):
    L = s.split(',')
    print(L)
    swap_list = []
    for i in L:
        for j in i:
            if j.isupper():
                swap_list.append(j.lower())
            elif j.islower():
                swap_list.append(j.upper())
            else:
                swap_list.append(j)
            
    return ''.join(swap_list)
    
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
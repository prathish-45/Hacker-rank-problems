import textwrap

def wrap(string, max_width):
    """ count = 0
    L = []
    for i in string:
        L.append(i)
    for i in L:
        print(i, end='')
        count += 1
        if count == max_width:
            print()
            count = 0 """
    wrapper = textwrap.TextWrapper(width=4)
    print(wrapper.fill(string))
    
            
            
    
    # print(L)
    # return L

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
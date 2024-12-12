def solve(s):
    L = []
    l = s.split(" ") 
    for i in l:
       if i.isdigit() == True:
           L.append(i)
       else:
           L.append(i.capitalize())
       
    return " ".join(L)
    
s = input()
result = solve(s)
print(result)
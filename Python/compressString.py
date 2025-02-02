def compresstheString(s):
    for i in range(len(s)):
        count = s.count(s[i])
        print(count)
        

s = "1222311"
compresstheString(s)
from collections import Counter

def company_logo(word):
    result = []
    dic = {}
    for i in range(len(word)):
        if word[i] not in dic:
            count = word.count(word[i])
            dic[count] = word[i]
    s_dic = dict(Counter(dic).most_common())   #incomplete
    print(s_dic)
        
        
        
        
    

if __name__ == "__main__":
    word = "aabbbccde"
    company_logo(word)
import time
start_time = time.time()    

def process_input(name):
    b = name.split(";")
    if b[0] == "S":
        return split_camel_case(b)
    else:
        return combine_camel_case(b)
    
def split_camel_case(a):
    start = 0
    words = []
    method, class_name, variable = a[2], a[2], a[2]
    if a[1] == "M":
        for i in range(1, len(method)):
            if method[i].isupper():
                words.append(method[start:i].lower())
                start = i
        words.append(method[start:].lower().replace("()", ""))
        return " ".join(words)
                
    elif a[1] == "C":
        for i in range(1, len(class_name)):
            if class_name[i].isupper():
                words.append(class_name[start:i].lower())
                start = i

        words.append(class_name[start:].lower())
        return " ".join(words)
        
    elif a[1] == "V":
        for i in range(1, len(variable)):
            if variable[i].isupper():
                words.append(variable[start:i].lower())
                start = i

        words.append(variable[start:].lower())
        return " ".join(words)
        
def combine_camel_case(a):
    words, method_list, class_list, variable_list = [], [], [], []
    method, class_name, variable = a[2], a[2], a[2]
    if a[1] == "M":
        words = method.split(" ")
        for i in words:
            if i == words[0]:
                pass
            else:
                method_list.append(i.capitalize())
        method_list.insert(0, words[0])
        method_list.append("()")
        return "".join(method_list)
            
    elif a[1] == "C":
        words = class_name.split(" ")
        for i in words:
            class_list.append(i.capitalize())
        return "".join(class_list)
        
    elif a[1] == "V":
        words = variable.split(" ")
        for i in words:
            if i == words[0]:
                pass
            else:
                variable_list.append(i.capitalize())
        variable_list.insert(0, words[0])
        return "".join(variable_list)         

input_string = input()
result = process_input(input_string)
print(result)
print("--- %s seconds ---" % (time.time() - start_time))

""" def process_input(name):
    a = name.split(";")
    start = 0
    words = []

    if a[0] == "S":
        if a[1] == "M":
            method = a[2]
            for i in range(1, len(method)):
                if method[i].isupper():
                    words.append(method[start:i].lower())
                    start = i
            words.append(method[start:].lower().replace("()", ""))
            return " ".join(words)
                    
        elif a[1] == "C":
            class_name = a[2]
            words = []
            start = 0

            for i in range(1, len(class_name)):
                if class_name[i].isupper():
                    words.append(class_name[start:i].lower())
                    start = i

            words.append(class_name[start:].lower())
            return " ".join(words)
            
        elif a[1] == "V":
            variable = a[2]
            words = []
            start = 0

            for i in range(1, len(variable)):
                if variable[i].isupper():
                    words.append(variable[start:i].lower())
                    start = i

            words.append(variable[start:].lower())
            return " ".join(words)
            
        
    elif a[0] == "C":
        if a[1] == "M":
            method = a[2]
            method_list = []
            words = method.split(" ")
            for i in words:
                if i == words[0]:
                    pass
                else:
                    method_list.append(i.capitalize())
            method_list.insert(0, words[0])
            method_list.append("()")
            return "".join(method_list)
            
        elif a[1] == "C":
            class_name = a[2]
            class_list = []
            words = class_name.split(" ")
            for i in words:
                class_list.append(i.capitalize())
            return "".join(class_list)
            
        elif a[1] == "V":
            variable = a[2]
            variable_list = []
            words = variable.split(" ")
            for i in words:
                if i == words[0]:
                    pass
                else:
                    variable_list.append(i.capitalize())
            variable_list.insert(0, words[0])
            return "".join(variable_list)
            
 """
    
# input_string = input()
# result = process_input(input_string)
# print(result)

""" import re
import sys
# Enter your code here. Read input from STDIN. Print output to STDOUT

def split_word(word):
    word = re.sub(r'\(\)$', r'', word)        
    word = re.sub(r'(?<!^)([A-Z])', r' \1', word)
    word = word.lower()
    print(word)
    
    
def combine_word(word, word_type):
    word = word.strip()
    if word_type == 'M':
        word = word + "()"
    elif word_type == 'C':
        word = word.capitalize()
    word = re.sub(r'\s([a-z])', lambda x: x.group(1).upper(), word)
            
    print(word)


def camelCase(action, word_type, word):
    if action == 'S':
        split_word(word)
    elif action == 'C':
        combine_word(word, word_type)

input_lines = sys.stdin.read().strip().split('\n')
for line in input_lines:
    action, word_type, word = line.split(';')
    camelCase(action, word_type, word) """
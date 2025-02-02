def minion_game(string):
    stuart = kevin = 0
    str_len = len(string)
    
    for i in range(str_len):
        if string[i] in 'AEIOU':
            kevin += str_len - i
        else:
            stuart += str_len - i
    
    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print('Draw')

        

if __name__ == '__main__':
    s = input()
    minion_game(s)
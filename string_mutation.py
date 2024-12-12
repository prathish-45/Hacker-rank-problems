def count_substring(string, sub_string):
    count = 0
    start = 0
    
    while True:
        start = string.find(sub_string, start)
        if start == -1:  # No more occurrences found
            break
        count += 1
        start += 1  # Move forward to allow overlapping matches
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

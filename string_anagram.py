from collections import defaultdict

def stringAnagram(dictionary, query):
    # Create a frequency dictionary for the sorted words in the dictionary
    freq_dict = defaultdict(int)
    for word in dictionary:
        sorted_word = ''.join(sorted(word))
        # print(sorted_word)
        freq_dict[sorted_word]  = freq_dict[sorted_word] + 1
        print(freq_dict)

    # For each query, count the occurrences of the sorted query in the frequency dictionary
    result = []
    for q in query:
        sorted_query = ''.join(sorted(q))
        result.append(freq_dict[sorted_query])

    return result

# print(stringAnagram(['heater', 'cold', 'clod', 'reheat', 'docl'], ['codl', 'heater', 'abcd']))  # Expected Output: [2, 3, 0]
print(stringAnagram(['heater', 'cold', 'clod', 'reheat', 'docl'], ['codl', 'heater', 'abcd']))  # Expected Output: [2, 3, 0]
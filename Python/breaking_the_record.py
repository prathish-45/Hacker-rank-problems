def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]
    min = 0
    max = 0
    break_score = []
    
    for i in range(len(scores)):
        if scores[i] < minimum:
            minimum = scores[i]
            min += 1
        elif scores[i] > maximum:
            maximum = scores[i]
            max += 1
            
        break_score.append([i, scores[i], minimum, maximum, min, max])
    return break_score

scores = []
for i in range(4):
    value = int(input("Enter the score: "))
    scores.append(value)
    
result = breakingRecords(scores)
print(breakingRecords)
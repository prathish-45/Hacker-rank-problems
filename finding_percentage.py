if __name__ == '__main__':
    # n = int(input())
    # student_marks = {}
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
    student_marks = {
        'Krishna': [67, 68, 69],
        'Arjun': [70, 98, 63],
        'Malika': [52, 56, 60]
    }
    query_name = 'Malika'
    
    # Find the average of the scores for the student
    query_scores = student_marks[query_name]
    print(query_scores)
    print("{0:.2f}".format(sum(query_scores) / len(query_scores)))
    
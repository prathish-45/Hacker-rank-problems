""" 
sample input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

sample output:
Berry
Harry

"""

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Extract all the grades and find the second lowest grade
    sorted_grade = []
    for grade in students:
        sorted_grade.append(grade[1])
    sorted_grade = list(sorted(set(sorted_grade)))
    print(sorted_grade)
    
    # Ensure there are at least two different grades
    if len(sorted_grade) < 2:
        print("Not enough unique grades to determine the second lowest.")
    else:
        second_lowest_grade = sorted_grade[1]
        
        # Find all students with the second lowest grade
        result = []
        for student in students:
            if student[1] == second_lowest_grade:
                result.append(student[0])
        
        # Sort the names alphabetically
        result = sorted(result)
        
        # Print each name on a new line
        for name in result:
            print(name)
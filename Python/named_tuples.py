# from collections import namedtuple

# Average = namedtuple('Average', 'ID MARKS NAME CLASS')
# n = int(input())
# fields = input().split()
# # print(fields)

# total = 0
# for i in range(n):
#     students = Average(*input().split())
#     # print(students)
#     total += int(students.MARKS)
    
# print(total/n)

from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())

total = 0
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
    
print('%.2f' % (total/n))

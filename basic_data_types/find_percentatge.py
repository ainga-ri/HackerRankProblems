n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split() 
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for key in student_marks:
    if (query_name == key):
        avarage = student_marks[key]
        
avarage_number = sum(avarage) / len(avarage)
formatted_number = "{:.2f}".format(avarage_number)
print(formatted_number)
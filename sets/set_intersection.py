# Problem of .intersection() concept

'''
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.

Students have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
Your task is to find the total number of students who have subscribed to both newspapers.
'''

students_subs_english = int(input("Enter de number of students subscribed to the English newspaper: "))

# To recieve a set at a time e.g. {1 2 3 4 5} and not 1 intro 2 intro 3 WE USE MAP. If it's the second, we used lists as it is commented below.
numbers_eng_students = set(map(int, input("").split()))
'''
for i in range(0,students_subs_english):
    ele = int(input())
    numbers_eng_students.add(ele)
'''

students_subs_french = int(input("Enter de number of students subscribed to the French newspaper: "))
numbers_fre_students = set(map(int, input("").split()))
'''
for i in range(0,students_subs_french):
    ele = int(input())
    numbers_fre_students.add(ele)
'''
both_students = numbers_eng_students.symmetric_difference(numbers_fre_students)
print(len(both_students))

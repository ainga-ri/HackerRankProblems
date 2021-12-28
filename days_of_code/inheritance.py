class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber) # en vez de repetir codigo, utilizando super() podemos utilizar los parametros de la superclase
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        number = 0
        mark = 0
        while (number != len(self.scores)):
            mark += self.scores[number]
            number += 1
        mark = mark / len(self.scores)
            
        if (90 <= mark <= 100):
            mark_letter = 'O'
        elif (80 <= mark < 90):
            mark_letter = 'E'
        elif (70 <= mark < 80):
            mark_letter = 'A'
        elif (55 <= mark < 70):
            mark_letter = 'P'
        elif (40 <= mark < 55):
            mark_letter = 'D'
        else:
            mark_letter = 'T'
            
        return mark_letter
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
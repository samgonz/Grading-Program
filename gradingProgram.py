#Dictionary that lists students and their class scores.
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#Empty Dictionary to hold students overall grade
student_grades = {}

#Loops through the students scores and assigns it a grade description based off the students score.
for i in student_scores:
    if student_scores[i] >= 91:
        student_grades[i] = 'Outstanding'
    elif student_scores[i] >= 81:
        student_grades[i] = 'Exceeds Expectations'
    elif student_scores[i] >= 71:
        student_grades[i] = 'Acceptable'
    else:
        student_grades[i] = 'Fail'
        
#Prints out the student_grades dictionary
print(student_grades)

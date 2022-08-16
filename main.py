student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  temp=int(student_scores[key])
  print(temp)
  if (temp>90):
    student_grades[key]= "Outstanding"
  elif (temp>80) and (temp<=90):
    student_grades[key]= "Exceeds Expectations"
  elif (temp>70) and (temp<=80):
    student_grades[key]= "Acceptable"
  else:
    student_grades[key]= "Fail" 
  print(student_grades)

# 🚨 Don't change the code below 👇
print(student_grades)






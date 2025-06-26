import pandas as pd

def grade(average_score):
  if average_score >= 90:
    return "A"
  elif average_score >= 80:
    return "B"
  elif average_score >= 70:
    return "C"
  elif average_score >= 60:
    return "D"
  else:
    return "F"

report_card = []

students = {
  "Alice": [85, 90, 92],
  "Bob": [72, 65, 70],
  "Charlie": [95, 98, 99],
  "Daisy": [60, 58, 64]
}
for key, value in students.items():
  average_score = sum(value) / len(value)
  total = sum(value)
  score = grade(average_score)
  
  print(f'{key} got an average score of {average_score:.2f}')
  print(f'{key} got total marks of {total:.2f}')
  print(f'{key} got a final grade of {score}')
  
  report_card.append({
    "Name": key,
    "Average":f' {average_score:.2f}',
    "Marks":f' {total:.2f}',
    "grade": score
  })

user_menu = """
a: add a student
v: view all reports
r: remove student
vs: view all students
"""

def add_student(name, number):
  students[name] = number
  
def view_all_reports():
  print(report_card)
  
def remove_student():
  if name1 in students:
    del students[name1]
  else:
    print(f"{name1} does not exist in list. ")
    
def view_students():
  print(students)

while True:
  print(user_menu)
  choice = input("What would you like to do? ")
  if choice == "a":
    name = input("Enter the student's name. ")
    marks = input("Enter the student's marks separated by commas. ")
    number = [int(num) for num in marks.split(',')]
    add_student(name, number)
  elif choice == "v":
    view_all_reports()
  elif choice == "vs":
    view_students()
  else:
    name1 = input("Enter the student's name. ")
    remove_student()
    
df = pd.DataFrame(report_card)
df.to_csv("Student_report_card.csv")



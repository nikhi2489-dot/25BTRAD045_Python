# Student Grading Automation
name = input("Enter student name: ")
marks1 = float(input("Enter marks in Subject 1: "))
marks2 = float(input("Enter marks in Subject 2: "))
marks3 = float(input("Enter marks in Subject 3: "))
total = marks1 + marks2 + marks3
percentage = total / 3
if percentage >= 90:
grade = "A+"
elif percentage >= 80:
grade = "A"
elif percentage >= 70:
grade = "B"
elif percentage >= 60:
grade = "C"
elif percentage >= 50:
grade = "D"
else:
grade = "F"
print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

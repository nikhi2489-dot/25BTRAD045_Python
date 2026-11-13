students = {}

def add_student():
name = input("Enter student name: ")
students[name] = {"Present": 0, "Absent": 0}
print("Student added successfully!")

def mark_attendance():
name = input("Enter student name: ")

if name in students:
status = input("Enter status (P/A): ").upper()

if status == "P":
students[name]["Present"] += 1
print("Marked Present")
elif status == "A":
students[name]["Absent"] += 1
print("Marked Absent")
else:
print("Invalid status")
else:
print("Student not found")

def display_attendance():
print("\n--- Attendance Details ---")

for name, record in students.items():
total = record["Present"] + record["Absent"]

if total > 0:
percentage = (record["Present"] / total) * 100
else:
percentage = 0

print("Name:", name)
print("Present:", record["Present"])
print("Absent:", record["Absent"])

print("Attendance:", percentage, "%")

def check_shortage():
threshold = float(input("Enter attendance threshold: "))

for name, record in students.items():
total = record["Present"] + record["Absent"]

if total > 0:
percentage = (record["Present"] / total) * 100
else:
percentage = 0

if percentage < threshold:
print(name, "has low attendance:", percentage, "%")

while True:
print("\n1. Add Student")
print("2. Mark Attendance")
print("3. Display Attendance")
print("4. Check Low Attendance")
print("5. Exit")

choice = input("Enter your choice: ")

if choice == "1":
add_student()
elif choice == "2":
mark_attendance()

elif choice == "3":
display_attendance()
elif choice == "4":
check_shortage()
elif choice == "5":
print("Thank you!")
break
else:
print("Invalid choice")

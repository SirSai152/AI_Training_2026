grade = ('Excellent', 'Good', 'Pass', 'Poor')
students = []
def calculate_average(scores):
	if len(scores) == 0:
		return 0
	else:
		return sum(scores)/len(scores)

	
def classify_score(scores):
	if scores <0 or scores > 100:
		return "Invalid"
	if scores >= 80:
		return grade[0]
	elif scores >= 60:
		return grade[1]
	elif scores >= 40:
		return grade[2]
	else:
		return grade[3]

def count_passed(scores):
	pass_score = 0
	for score in scores:
		if score >= 40:
			pass_score += 1
	return pass_score

for i in range(5):
	
	print(f"Enter details for student {i + 1}:")
	name = str(input("Name: "))
	Age = int(input("Age: "))
	study_hours = str(input("StudyHours: "))
	scores = float(input("PythonScore: "))
	students.append({"name": name, "age": Age,"study_hours": study_hours, "mark": scores})

print("===== STUDENT PERFORMANCE REPORT =====")
for student in students:
	print(
		f"Name: {student['name']}\n "
		f"Age: {student['age']}\n "
		f"StudyHours: {student['study_hours']}\n "
		f"PythonScore: {student['mark']}\n"
		f"Grade: {classify_score(student['mark'])}"
	)
print("===== SUMMARY =====")
print("Total Students:", len(students))
all_scores = [student["mark"] for student in students]
py_point = calculate_average(all_scores)
print("Average Score:", py_point)
print("Highest Score:", max(all_scores))
print("Lowest Score:", min(all_scores))
result = count_passed(all_scores)
print("Passed Students:", result)
print("Failed Students:", len(students) - result)
top_student = max(students, key=lambda student: student["mark"])
print("Top Student:", top_student["name"])
 


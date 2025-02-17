students = [
    ("student_a", [20, 20, 25]),
    ("student_b", [45, 30, 50]),
    ("student_c", [90, 95, 85]),
    ("student_d", [90, 95, 85]),
    ("student_e", [22, 25, 25]),
]
list = [(name, round(sum(scores) / len(scores), 2)) for name, scores in students]
for name, avg in list:
    print(f"{name} Average Score: {avg}")
highest = max(avg for _, avg in list)
top = [name for name, avg in list if avg == highest]
print("\nTop Scorer(s):")
print(top)
fail= [name for name, avg in list if avg < 40]
if fail:
    print("\nStudents who failed:")
    print(fail)
else:
    print("\nNo students failed.")

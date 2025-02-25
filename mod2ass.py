import csv
import os

class Student:
    students = []

    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age  
        self.grade = grade
        Student.students.append(self)
    @property
    def age(self):
        return self.age1
    @property
    def grade(self):
        return self.grade1
    @age.setter
    def age(self, correct_age):
        if correct_age > 4:
            self.age1 = correct_age
        else:
            raise ValueError("Age shoulb be greater than 4 .")
    @grade.setter
    def grade(self, correct_grade):
        if correct_grade in ["A", "B", "C", "D", "E", "F"]:
            self.grade1 = correct_grade
        else:
            raise ValueError("Invalid grade. ")
    @staticmethod
    def create_csv(filename = "students.csv"):
        if not os.path.exists("students.csv"):
            with open("students.csv", "w", newline="") as f1:
                writer = csv.writer(f1)
                writer.writerow(["ID", "Name", "Age", "Grade"])

    @staticmethod
    def save_to_csv(filename = "students.csv"):
        with open("students.csv", "w", newline="") as f2:
            writer = csv.writer(f2)
            writer.writerow(["ID", "Name", "Age", "Grade"])
            for student in Student.students:
                writer.writerow([student.student_id, student.name, student.age, student.grade])
    @staticmethod
    def read_from_csv(filename = "students.csv"):
        with open("students.csv", "r") as f3:
            reader = csv.reader(f3)
            for row in reader:
                print(row)

    @staticmethod
    def add_record(student,filename = "students.csv"):
        with open("students.csv", "a", newline="") as f4:
            writer = csv.writer(f4)
            writer.writerow([student.student_id, student.name, student.age, student.grade])

    @staticmethod
    def modify_record(student_id, new_name, new_age, new_grade,filename = "students.csv"):
        updated_rows = []
        with open("students.csv", "r") as f5:
            reader = csv.reader(f5)
            for row in reader:
                if row[0] == str(student_id):
                    row[1] = new_name
                    row[2] = new_age 
                    row[3] = new_grade
                updated_rows.append(row)

        with open("students.csv", "w", newline="") as f6:
            writer = csv.writer(f6)
            writer.writerows(updated_rows)

    @staticmethod
    def delete_record(student_id,filename = "students.csv"):
        updated_rows = []
        with open("students.csv", "r") as f7:
            reader = csv.reader(f7)
            updated_rows = [row for row in reader if row[0] != str(student_id)]

        with open("students.csv", "w", newline="") as f8:
            writer = csv.writer(f8)
            writer.writerows(updated_rows)

    @staticmethod
    def search_record(student_id,filename = "students.csv"):
        with open("students.csv", "r") as f9:
            reader = csv.reader(f9)
            for row in reader:
                if row[0] == str(student_id):
                    print("Record Found:", row)
                    return
        print("Record Not Found.")
Student.create_csv()
try:
    s1 = Student(1, "Veer", 20, "A")
    s2 = Student(2, "Sheeru", 22, "B")
    s3 = Student(3, "vikram", 21, "C")
    s4 = Student(4, "raju",19,"F")

except ValueError as e :
    print("Error :" , e )
Student.save_to_csv()
print("\nStudent Records:")
Student.read_from_csv()
s1.age = 24 
print(s1.age , s1.name)
s2.grade = "F"
print(s1.grade , s1.name)
Student.modify_record(2,"rishab",22, "A")
print("\nSearching for Student ID 1:")
Student.search_record(2)
Student.delete_record(3)
print("\nFinal Student Records:")
Student.read_from_csv()

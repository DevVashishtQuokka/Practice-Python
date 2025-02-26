import csv 
import os
class Student:
    students = []

    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = self.set_age(age)  
        self.grade = self.set_grade(grade)
        Student.students.append(self)

    def set_age(self, age):
        if age > 4:
            return age
        else:
            print("Age should be greater than 4.")
    def get_age(self):
        return self.age
    def set_grade(self, grade):
        if grade in ["A","B","C","D","E","F"]:
            return grade
        else:
            print("Invalid Grade.")
    def get_grade(self):
        return self.grade
    
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
    def get_student_id(self):
        return self.student_id
    @staticmethod
    def record_exists(students, filename="students.csv"):
        if not os.path.exists(filename):
            return False
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] == str(students.get_student_id()):
                    return True
        return False
    @staticmethod
    def add_record(student,filename = "students.csv"):
        if Student.record_exists(student, filename):
            raise ValueError("Duplicate record: Student with this ID already exists.")
        with open("students.csv", "a", newline="") as f4:
            writer = csv.writer(f4)
            writer.writerow([student.student_id, student.name, student.age, student.grade])
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
s1 = Student(1, "Veer", 20, "A")
s2 = Student(2, "Sheeru", 22, "B")
s3 = Student(3, "vikram", 21, "C")
s4 = Student(4, "raju",19,"F")
Student.create_csv()
Student.save_to_csv()
print("\nStudent Records:")
Student.read_from_csv()
print(s1.get_age())
s5 = Student(1,"heer" , 20 , "C")
Student.add_record(s5)
  

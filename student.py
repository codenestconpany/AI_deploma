import builtins
import arabic_reshaper
from bidi.algorithm import get_display

def _ar(val):
    if isinstance(val, str):
        return get_display(arabic_reshaper.reshape(val))
    return val

_orig_print = builtins.print
_orig_input = builtins.input

def print(*args, **kwargs):
    _orig_print(*(_ar(arg) for arg in args), **kwargs)

def input(prompt=""):
    return _orig_input(_ar(prompt))

# -------------------------------------------------------------

class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def calculate_averagre(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_grade_letter(self):
        avg = self.calculate_averagre()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def get_min_max_grades(self):
        if len(self.grades) == 0:
            return 0, 0
        return max(self.grades), min(self.grades)

    def display_info(self):
        avg = self.calculate_averagre()
        letter = self.get_grade_letter()
        max_grade, min_grade = self.get_min_max_grades()
        print("-" * 40)
        print("اسم الطالب   :", self.name)
        print("الرقم الجامعي   :", self.student_id)  
        print("الدرجات     :", self.grades)
        print("المعدل النهائي     :", avg)
        print("التقدير العام   :", letter)
        print("اعلى درجة     :", max_grade)
        print("اقل درجة    :", min_grade)
        print("-" * 40)


def search_student(students_list, target_id):
    found = False
    for student in students_list:
        if student.student_id == target_id:
            print("\n[تم العثور على سجل الطالب]")
            student.display_info()
            found = True
            break
    if not found:
        print(f"\n[الطالب صاحب الرقم الجامعي {target_id} غير مسجل بالنظام]")  # إضافة f للـ string


def main():
    Students_database = []
    total_students = int(input("ادخل عدد الطلاب الاجمالي المراد تسجيلهم: "))

    for i in range(total_students):
        print(f"\n--ادخل بيانات الطالب({i + 1})--")
        name = input("اسم الطالب: ")
        student_id = input("الرقم الجامعي: ")
        grades_count = int(input("عدد الدرجات الخاصة بهذا الطالب: "))
        
        grades = []
        for j in range(grades_count):
            grade = float(input(f"ادخل الدرجة ({j + 1}): "))
            grades.append(grade)  # إضافة الدرجة إلى قائمة الدرجات

        # تصحيح الإزاحة لتكون داخل حلقة الطلاب
        student_object = Student(name, student_id, grades)
        Students_database.append(student_object)

    print("\n================ تقارير جميع الطلاب ================")
    for student in Students_database:
        student.display_info()

    # نقل عملية البحث خارج حلقة الطباعة
    search_id = input("\nادخل الرقم الجامعي للبحث عن طالب محدد: ")
    search_student(Students_database, search_id)


main()
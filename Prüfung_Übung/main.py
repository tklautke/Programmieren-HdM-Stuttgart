from Prüfung_Übung.SchoolClass import SchoolClass
from Prüfung_Übung.Student import Student
from Prüfung_Übung.Teacher import Teacher

if __name__ == '__main__':
    """
    -> New Students
    """
    robin = Student(name="Robin", sex="male", age=19, semester=1, matrikel=1454)
    markus = Student("Markus", 19, "male", 87645, 1)
    theo = Student("Theo", 20, "male", 23344, 1)

    """
    -> New Teacher
    """
    mr_klotz = Teacher("Mr. Klotz", 35, "male")

    """
    -> New Class
    """
    school_class_1 = SchoolClass(mr_klotz)

    print(str(robin))
    print(str(mr_klotz))

    # Add Theo and Robin to Class
    school_class_1.add_student_to_class(robin, theo)

    # Add Markus to the Class of Robin and Theo
    school_class_1.add_student_to_class(markus)

    school_class_1.show_name_of_students_in_class()

    print(robin.get_semester())

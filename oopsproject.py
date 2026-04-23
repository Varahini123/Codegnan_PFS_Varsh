'''
#Base class
class Institute:
    name = "K Hema Varshini"
    phone = "8074460056"
    gender = "Female"
    age = 22
    institute_name = "Codegnan"
    course_name = "Python fullstack"
    
    @staticmethod
    def display():
        print(f"Student name: {Institute.name}")
        print(f"Phone number: {Institute.phone}")
        print(f"Gender: {Institute.gender}")
        print(f"Age: {Institute.age}")
        print(f"Institute: {Institute.institute_name}")
        print(f"Course_name: {Institute.course_name}")
        print()

class PythonLecture:
    name = "Bhanu Teja"
    course = "Python"
    course_id = "PFS-001"
    student_count = 3
    
    @staticmethod
    def display():
        print(f"Lecture name: {PythonLecture.name}")
        print(f"Course: \"{PythonLecture.course}\"")
        print(f"ID: {PythonLecture.course_id}")
        print(f"Student joined: [{PythonLecture.student_count}]")
        print()
        PythonStudent1.display()
        PythonStudent2.display()
        PythonStudent3.display()

class PythonStudent1:
    name = "Divya Sree"
    student_id = "PFS-01"
    
    @staticmethod
    def display():
        print(f"name: '{PythonStudent1.name}'")
        print(f"ID: {PythonStudent1.student_id}")
        print()

class PythonStudent2:
    name = "Likitha"
    student_id = "PFS-02"
    
    @staticmethod
    def display():
        print(f"name: '{PythonStudent2.name}'")
        print(f"ID: {PythonStudent2.student_id}")
        print()

class PythonStudent3:
    name = "Hema"
    student_id = "PFS-03"
    
    @staticmethod
    def display():
        print(f"name: '{PythonStudent3.name}'")
        print(f"ID: {PythonStudent3.student_id}")
        print()

class JavaLecture:
    name = "Naveen"
    course = "Java"
    course_id = "JFS-001"
    student_count = 2
    
    @staticmethod
    def display():
        print(f"Lecture name: {JavaLecture.name}")
        print(f"Course: \"{JavaLecture.course}\"")
        print(f"ID: {JavaLecture.course_id}")
        print(f"Student joined: {JavaLecture.student_count}")
        print()
        JavaStudent1.display()
        JavaStudent2.display()

class JavaStudent1:
    name = "Kavya"
    student_id = "JFS-01"
    
    @staticmethod
    def display():
        print(f"name: '{JavaStudent1.name}'")
        print(f"ID: {JavaStudent1.student_id}")
        print()

class JavaStudent2:
    name = "Kundana"
    student_id = "JFS-02"
    
    @staticmethod
    def display():
        print(f"name: '{JavaStudent2.name}'")
        print(f"ID: {JavaStudent2.student_id}")
        print()

# Run everything - no objects created, just call static methods
Institute.display()
PythonLecture.display()
JavaLecture.display()












































































































    

from counselor_module import Counselor
from student_module import NormalStudent, UrgentStudent
from consultation_module import ConsultationSystem

def init_consultation_system():
    system = ConsultationSystem("Hong Kong Metropolitan University")
    counselors = [
        Counselor("C001", "Mr. Li", "Academic Stress", "Mon-Fri 9:00-17:00"),
        Counselor("C002", "Ms. Wang", "Emotion Regulation", "Tue-Sat 10:00-18:00"),
        Counselor("C003", "Mr. Zhang", "Interpersonal Relationships", "Wed-Sun 13:00-20:00")
    ]
    for c in counselors:
        system.add_counselor(c)
    students = [
        NormalStudent("S001", "Zhang San", "Year 2", "Computer Science"),
        NormalStudent("S002", "Zhao Wu", "Year 1", "Electronic Engineering"),
        UrgentStudent("S003", "Li Si", "Year 3", "Software Engineering")
    ]
    for s in students:
        system.add_student(s)
    return system

if __name__ == "__main__":
    print("===== HKMU Campus Psychological Counseling System (Pre-submission Version) =====")
    system = init_consultation_system()
    print("\n【1. Counselor List】")
    for c in system._ConsultationSystem__counselors:
        print(c)
    print("\n【2. Student Appointment Demo】")
    print(system.make_appointment("S003", "Emotion Regulation", "2026-03-10 14:00"))
    print(system.make_appointment("S001", "Academic Stress", "2026-03-11 10:00"))
    print("\n【3. All Appointment Records】")
    print(system.show_all_appointments())
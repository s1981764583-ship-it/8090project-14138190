from counselor_module import Counselor
from student_module import NormalStudent, UrgentStudent

class ConsultationSystem:
    def __init__(self, school_name):
        self.__school_name = school_name
        self.__counselors = []
        self.__students = []
        self.__appointments = []
    def get_all_counselors(self):
        return self.__counselors.copy()

    def add_counselor(self, counselor):
        if isinstance(counselor, Counselor) and counselor not in self.__counselors:
            self.__counselors.append(counselor)
            return f"Counselor {counselor.get_name()} added to {self.__school_name} Counseling Center!"
        return "Counselor already exists or invalid type!"

    def add_student(self, student):
        if isinstance(student, (NormalStudent, UrgentStudent)) and student not in self.__students:
            self.__students.append(student)
            return f"Student {student.get_name()} registered in counseling system!"
        return "Student already exists or invalid type!"

    def make_appointment(self, student_id, field, date_time):
        student = next((s for s in self.__students if s.get_student_id() == student_id), None)
        if not student:
            return "Student not registered!"

        available_counselors = [c for c in self.__counselors if c.get_field() == field and c.get_status() == "Available"]
        if not available_counselors:
            return f"No available counselors for {field}, please change time or field!"

        if isinstance(student, UrgentStudent):
            counselor = available_counselors[0]
        else:
            counselor = available_counselors[0]

        appointment_id = f"AP{len(self.__appointments)+1:03d}"
        appointment = {
            "id": appointment_id,
            "student": student.get_name(),
            "counselor": counselor.get_name(),
            "field": field,
            "time": date_time,
            "status": "Booked"
        }
        self.__appointments.append(appointment)
        counselor.set_status("Busy")
        student.add_consult_record(f"{date_time} Consultation with {counselor.get_name()} ({field}) | Appointment ID: {appointment_id}")

        return (f"Appointment Success!\nAppointment ID: {appointment_id}\nStudent: {student.get_name()}\n"
                f"Counselor: {counselor.get_name()}\nField: {field}\nTime: {date_time}")

    def show_all_appointments(self):
        if not self.__appointments:
            return "No appointment records!"
        res = [f"=== {self.__school_name} Counseling Appointment Records ==="]
        for ap in self.__appointments:
            res.append(f"【{ap['id']}】{ap['student']} - {ap['counselor']} | {ap['field']} | {ap['time']} | {ap['status']}")
        return "\n".join(res)
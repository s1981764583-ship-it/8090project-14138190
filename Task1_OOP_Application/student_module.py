from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, student_id, name, grade, major):
        self.__student_id = student_id
        self.__name = name
        self.__grade = grade
        self.__major = major
        self.__consult_records = []

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_grade(self):
        return self.__grade

    def add_consult_record(self, record):
        self.__consult_records.append(record)
        return f"Added consultation record for {self.__name}: {record}"

    def show_consult_records(self):
        if not self.__consult_records:
            return f"{self.__name} has no consultation records"
        return f"{self.__name}'s consultation records: {self.__consult_records}"

    @abstractmethod
    def get_consult_priority(self):
        pass

class NormalStudent(Student):
    def get_consult_priority(self):
        return f"Normal Student【{self.get_name()}】: Priority - Normal, arranged by appointment order"

class UrgentStudent(Student):
    def get_consult_priority(self):
        return f"Urgent Student【{self.get_name()}】: Priority - Urgent, counselor arranged first"
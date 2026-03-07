class Counselor:
    total_counselors = 0
    FIELDS = ["Academic Stress", "Interpersonal Relationships", "Emotion Regulation", "Career Planning", "Family Issues"]

    def __init__(self, counselor_id, name, field, available_time):
        self.__counselor_id = counselor_id
        self.__name = name
        self.__field = field
        self.__available_time = available_time
        self.__status = "Available"
        Counselor.add_counselor_count()

    @classmethod
    def add_counselor_count(cls):
        cls.total_counselors += 1

    @staticmethod
    def is_valid_field(field):
        return field in Counselor.FIELDS

    def get_counselor_id(self):
        return self.__counselor_id

    def get_name(self):
        return self.__name

    def get_field(self):
        return self.__field

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        if new_status in ["Available", "Busy"]:
            self.__status = new_status
            return f"Counselor {self.__name} status updated to: {new_status}"
        raise ValueError("Status can only be 'Available' or 'Busy'")

    def __str__(self):
        return (f"【Counselor ID: {self.__counselor_id}】Name: {self.__name} | Field: {self.__field} "
                f"| Available Time: {self.__available_time} | Status: {self.__status}")

    def __add__(self, other):
        if isinstance(other, Counselor):
            return f"Joint Consultation: {self.__name} ({self.__field}) & {other.__name} ({other.__field})"
        raise TypeError("Only support concatenation between Counselor objects")
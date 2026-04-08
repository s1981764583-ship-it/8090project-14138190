from counselor_module import Counselor
from student_module import NormalStudent, UrgentStudent
from consultation_module import ConsultationSystem
import tkinter as tk
from tkinter import messagebox

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


def run_counseling_demo():

    result1 = system.make_appointment("S003", "Emotion Regulation", "2026-03-10 14:00")
    result2 = system.make_appointment("S001", "Academic Stress", "2026-03-11 10:00")

    total_result = f"{result1}\n\n{result2}\n\n{system.show_all_appointments()}"
    messagebox.showinfo("Counseling System Result", total_result)

system = init_consultation_system()

if __name__ == "__main__":

    print("===== HKMU Campus Psychological Counseling System (Final Version) =====")
    print("\n【1. Counselor List】")

    for c in system.get_all_counselors():
        print(c)
    
    root = tk.Tk()
    root.title("HKMU Campus Counseling System")  
    root.geometry("400x150")  
    root.resizable(False, False)  
    
    label = tk.Label(root, text="Click the button to run counseling demo:", font=("Arial", 10))
    label.pack(pady=20)  
    
    run_btn = tk.Button(
        root,
        text="Run Counseling Appointment Demo",
        command=run_counseling_demo,  
        font=("Arial", 10),
        width=30,  
        height=2  
    )
    run_btn.pack()
    
    root.mainloop()
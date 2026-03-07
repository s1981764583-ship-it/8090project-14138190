# Task1: OOP-based Campus Psychological Counseling Management System
## Module Description
This module is a Campus Psychological Counseling Management System, which fits the actual campus scenario and solves the practical problems of student counseling appointment, counselor management, and consultation record tracking. It strictly follows the course OOP requirements and implements all OOP concepts.

### Module Structure (≥3, meet course requirements)
1. counselor_module.py: Counselor class, encapsulation + class attributes + class methods + static methods + magic methods
2. student_module.py: Abstract base class Student + subclasses NormalStudent/UrgentStudent, inheritance + polymorphism + abstract ADT
3. consultation_module.py: ConsultationSystem class, aggregation of Counselor/Student objects, implement core business logic
4. main.py: Main program entry, call each module, implement interactive demonstration

### Implemented OOP Concepts
- Encapsulation (private attributes + getter/setter)
- Inheritance (abstract base class Student → subclasses NormalStudent/UrgentStudent)
- Polymorphism (different implementations of get_consult_priority)
- Abstraction (ABC abstract base class + @abstractmethod)
- Class attributes/class methods
- Static methods
- Magic methods
- Aggregation/composition
- Modular programming

### Running Method
Run main.py directly:
python main.py

### Future Plans
- Add functions of consultation record modification/deletion and counselor schedule management
- Add student privacy protection mechanism
- Implement simple GUI interface
- Add more boundary test cases

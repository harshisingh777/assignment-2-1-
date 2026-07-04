from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
@dataclass
class Student:
    student_id:int; name:str; department:str; email:str
    def enroll(self,course_code:str)->bool:return True
    def view_marks(self)->dict:return {}
class Enrollment:
    def __init__(self,eid:int,sid:int,code:str,marks:float=0): self.enrollment_id=eid; self.student_id=sid; self.course_code=code; self.marks=marks
    def update_marks(self,marks:float)->None:self.marks=marks
class WaitlistedEnrollment(Enrollment):
    pass
class EnrollmentRepository(ABC):
    @abstractmethod
    def save(self,e:Enrollment)->None:...
    @abstractmethod
    def find_by_student(self,sid:int)->List[Enrollment]:...
    @abstractmethod
    def delete(self,eid:int)->None:...

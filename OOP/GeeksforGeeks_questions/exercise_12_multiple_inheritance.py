# Implement the following classes to understand multiple inheritance in Python:

# Class Name: Student
# Attributes:
# sid (int) — Student ID.
# deptid (int) — Department ID.
# Constructor: __init__(self, sid, deptid) — Initializes the sid and deptid attributes.
# Method: get_info(self) — Returns a formatted string with the student ID and department ID, eg., "StudentID:101 DepartmentID:42"

# Class Name: Faculty
# Attributes:
# eid (int) — Employee ID.
# deptid (int) — Department ID.
# Constructor: __init__(self, eid, deptid) — Initializes the eid and deptid attributes.
# Method: get_info(self) — Returns a formatted string with the employee ID and department ID, eg., "EmployeeID:555 DepartmentID:42"

# Class Name: PhDStudent (Inherits from both Student and Faculty)
# Constructor: __init__(self, sid, eid, deptid) — Calls the constructors of Student and Faculty to initialize sid, eid, and deptid.
# Method: get_info(self) — Returns a formatted string with the student ID, employee ID and department ID, 
# eg., "Student ID:101 EmployeeID:555 DepartmentID:42".

# Example:
# Input: sid = 101, eid = 555, deptid = 42
# Output: 
# StudentID:101 DepartmentID:42
# EmployeeID:555 DepartmentID:42
# Student ID:101 EmployeeID:555 DepartmentID:42

class Student:
    '''
    Represent Student with attributes student id(sid) and department id(deptid)
    '''
    def __init__(self, sid: int, deptid: int):
        '''
        initialize student object
        
        Args:
            sid (int): id of the student
            deptid (int): department id of student
        '''
        self.sid = sid
        self.deptid = deptid
        
    def get_info(self) -> str:
        '''
        gets information of the student
        
        Returns:
            str: returns student details
        '''
        return f"Student Id: {self.sid}, Department Id: {self.deptid}"
    
class Faculty:
    '''
    Represent Faculty with attributes employee id(eid) and department id(deptid)
    '''
    def __init__(self, eid: int, deptid: int):
        '''
        initialize faculty object
        
        Args:
            eid (int): id of the faculty
            deptid (int): department id of faculty
        '''
        self.eid = eid
        self.deptid = deptid
        
    def get_info(self) -> str:
        '''
        gets information of the faculty
        
        Returns:
            str: returns faculty details
        '''
        return f"Employee Id: {self.eid}, Department Id: {self.deptid}"
    
class PhDStudent(Student, Faculty):
    '''
    Represents PhDStudent with attributes student id(sid), employee id(eid) and department id(deptid)
    
    this class is used to create objects, which gets information of the phdstudents
    '''
    def __init__(self, sid, eid, deptid):
        '''
        initialize phdstudent object
        
        Args:
            sid (int): id of the student
            eid (int): id of the employee
            deptid (int): department id of student
        '''
        Student.__init__(self, sid, deptid)
        Faculty.__init__(self, eid, deptid)
        
    def get_info(self) -> str:
        '''
        gets information of the faculty
        
        Returns:
            str: returns faculty details
        '''
        return f"Student Id: {self.sid}, Employee Id: {self.eid}, Department Id: {self.deptid}"
    
phdstudent = PhDStudent(45, 54, 4)
print(phdstudent.get_info())    
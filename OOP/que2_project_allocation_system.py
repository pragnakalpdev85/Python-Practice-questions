# Question 2: Employee Project Allocation System
# You are building a system to allocate employees to projects based on their skills, availability, and project priority. Each employee can work on only one project at a time. Each project requires a specific number of employees with certain skills and has a priority level.
# Your goal is to assign employees to the highest priority projects first, fulfilling their required skill sets as much as possible.
# The challenge is to maximize the number of fully staffed projects while respecting constraints.

# Rules & Constraints:
# One Project per Employee
# Each employee can be assigned to at most one project.
# Project Completion Criteria

# A project is considered staffed only if:
# The required number of employees is met (numPeopleRequired)
# The required skills are covered collectively by the assigned employees
# Priority-Based Allocation
# Projects with lower priority numbers are handled first.
# Skill Matching
# Employees may have overlapping skills.
# You must select a combination of available employees whose combined skill sets satisfy the requiredSkills of the project.
# No Built-in Functions Allowed
# You must not use .sort(), .filter(), .map(), .reduce(), etc.

# Example Input:
# employees = [
#   { id: "E1", skills: ["Python", "Django"], available: true },
#   { id: "E2", skills: ["React"], available: true },
#   { id: "E3", skills: ["Django"], available: true },
#   { id: "E4", skills: ["Java", "Spring"], available: true },
#   { id: "E5", skills: ["Java"], available: true },
#   { id: "E6", skills: ["Python"], available: false }
# ]

# projects = [
#   {
#     id: "P1",
#     requiredSkills: ["Python", "Django"],
#     numPeopleRequired: 2,
#     priority: 1
#   },
#   {
#     id: "P2",
#     requiredSkills: ["Java", "Spring"],
#     numPeopleRequired: 2,
#     priority: 2
#   },
#   {
#     id: "P3",
#     requiredSkills: ["React", "NodeJS"],
#     numPeopleRequired: 2,
#     priority: 3
#   }
# ]

# Expected Output:
# {
#   projectAssignments: {
#     P1: ["E1", "E6"],
#     P2: ["E4", "E5"]
#   },
#   unassignedEmployees: ["E2","E3"],
#   unstaffedProjects: ["P3"]
# }
import json

class AssignmentException(Exception):
    """AssignmentException class to throw custom errors inherits Exception class"""
    pass


class Employee:
    '''
    Represents employees
    
    This class provides functionalities like, is employe available ,employee assigned to project
    and assign employee to project
    
    Class Attribute:
        emp_list (list): list of employees
    
    Instance Attributes:
        id (str) :id of the employee
        skills (list[str]): list of skills of an employee
        available (bool): employee is availableor not
        project_id (str): id of project employee is assign to
    '''
    
    emp_list = []
    
    def __init__(self, id: str, skill: list, available = True, project_id = None):
        '''
        Initialize employee object
        
        Args:
            id (str) :id of the employee
            skills (list[str]): list of skills of an employee
            available (bool): employee is availableor not
            project_id (str): id of project employee is assign to
        ''' 
        self.__id = id
        Employee.emp_list.append(id)
        self.__skill = skill
        self.__available = available
        self.__project_id = project_id
        
    @staticmethod
    def validate_employee_data(data: dict) -> bool:
        '''
        validates employee data 
        
        Args:
            data (dict): dictionary of employee data
        Returns:
            bool: returns true if data is valid
        '''
        if not isinstance(data, dict):
            raise AssignmentException("Employee Data format is incorrect")
        if 'id' not in data:
            raise AssignmentException("There is no Id in employee")
        if 'skills' not in data:
            raise AssignmentException(f"There is no skills of employee with id {data['id']}")
        if 'available' not in data:
            raise AssignmentException(f"There is no available status in employee with id {data['id']}")
        if not isinstance(data['id'], str):
            raise AssignmentException(f"Employee has invalid id")
        if not isinstance(data['skills'],list):
            raise AssignmentException(f"Employee with id {data['id']} has invalid skills")
        if not isinstance(data['available'],bool):
            raise AssignmentException(f"Employee with id {data['id']} has invalid available status")
        
        return True
        
    def get_skills(self) -> list:
        '''
        Gets skills of employee
        
        Returns:
            list: list of skills of employee
        '''
        return self.__skill
    
    def get_id(self) -> str:
        '''
        Gets id of an employee
        
        Returns:
            str: id of an employee
        '''
        return self.__id
    
    def is_available(self) -> bool:
        '''
        Checks employee is available or not
        
        Returns:
            bool: employee is available or not
        '''
        return self.__available
    
    def assign(self, project_id: str) -> str:
        '''
        Assignes employee to a project
        
        Args:
            project_id (str): id of the project
            
        Retruns:
            str: employee id
        '''
        self.__project_id = project_id
        self.__available = False
        return self.__id
      
  
class Project:
    '''
    Represents project
    
    This class provides functionality like get_project_requirement, add employee,
    
    Attributes:
        id (str): id of the project
        priority (int): priority of the project
        required_skills (list): list of project requirements
        num_people_require (int): number of people require for the project
        employee_assigned (list): employee assigned to the project
    '''
    
    def __init__(self, id: str, num_people_require: int, required_skills: list, priority: int,employee_assigned = []):
        '''
        initializes project object
        
        Args:
            id (str): id of the project
            priority (int): priority of the project
            required_skills (list): list of project requirements
            num_people_require (int): number of people require for the project
            employee_assigned (list): employee assigned to the project
        '''
        self.__id = id
        self.__num_people_require = num_people_require
        self.__required_skills = required_skills
        self.__priority = priority
        self.__employee_assigned = employee_assigned
        
    @staticmethod
    def validate_project_data(data: dict) -> bool:
        '''
        validates project data 
        
        Args:
            data (dict): dictionary of project data
        Returns:
            bool: returns true if data is valid
        '''
        if not isinstance(data, dict):
            raise AssignmentException("Project Data format is incorrect")
        if 'id' not in data:
            raise AssignmentException("There is no Id in Project")
        if 'requiredSkills' not in data:
            raise AssignmentException(f"There is no requiredSkills of Project with id {data['id']}")
        if 'numPeopleRequired' not in data:
            raise AssignmentException(f"There is no numPeopleRequired in Project with id {data['id']}")
        if 'priority' not in data:
            raise AssignmentException(f"There is no priority in Project with id {data['id']}")
        if not isinstance(data['id'], str):
            raise AssignmentException(f"Project has invalid id")
        if not isinstance(data['requiredSkills'],list):
            raise AssignmentException(f"Project with id {data['id']} has invalid requiredSkills")
        if not isinstance(data['numPeopleRequired'],int):
            raise AssignmentException(f"project with id {data['id']} has invalid numPeopleRequired")
        if not isinstance(data['priority'],int):
            raise AssignmentException(f"project with id {data['id']} has invalid priority")
        
        return True
        
    def get_id(self) -> str:
        '''
        Gets id of the project
        
        Returns:
            str: id of the projecct
        '''
        return self.__id
        
    def get_required_skills(self) -> list:
        '''
        Gets list of requirement skills
        
        Returns:
            list: list of required skills
        '''
        return self.__required_skills
    
    def get_required_num_of_people(self) -> int:
        '''
        Gets number of people required
        
        Returns:
            int: number of people required
        '''
        return self.__num_people_require
        
    def assign_employees(self, emps: list):
        '''
        assignes employee to project
        
        Args:
            emp_id (str): list of employees
        '''
        self.__employee_assigned = []
        for emp in emps:
            self.__employee_assigned.append(emp.assign(self.__id))
            
    def is_staffed(self) -> bool:
        '''
        Chechks project is staffed or not
        
        Returns:
            bool: project is staffed or not
        '''
        if self.__employee_assigned != []:
            return True
        
        return False
    
    
class AllocateEmployee:
    '''
    Represents Employee allocation 
    
    This class provides functionality of allocating employee to projects
    
    Atrributes:
        project_assignment (dict): dictionary with assigned employees to projects
        unassigned_emp (list): list of unassigned employees
        unstaffed_projects (list): list of unstaffed projects
    '''
    
    def __init__(self, project_assignment = {}, unassigned_emp = [], unstaffed_projects = [], emp_list = [], project_list = []):
        '''
        initializes allocate employee objects
        
        Args:
            project_assignment (dict): dictionary with assigned employees to projects
            emp_list (list) = list of employees
            project_list (list) = list of projects
            unassigned_emp (list): list of unassigned employees
            unstaffed_projects (list): list of unstaffed projects
        '''
        self.__project_assignment = project_assignment 
        self.__unassigned_emp = unassigned_emp 
        self.__emp_list = emp_list
        self.__unstaffed_projects = unstaffed_projects 
        self.__project_list = project_list
        
    def convert_employee_list_to_object(self, employee_list) -> list:
        '''
        converts list of dictionary of employee to list of objects
        
        Args:
            employee_list (list): list of dictionaries of employee
        Returns:
            list: list of employee objects
        '''
        if employee_list == []:
            raise AssignmentException("Employee List is empty")
        emps = []
        for emp in employee_list:
            try:
                status = Employee.validate_employee_data(emp)
                if status:
                    emps.append(Employee(emp['id'],emp['skills']))
            except AssignmentException as e:
                print(e)
            
        return emps
    
    def sort_and_convert_project_list_to_objects(self, projects: list) -> list:
        '''
        converts list of dictionary of projects to list of objects and sort them by priority
        
        Args:
            employee_list (list): list of dictionaries of project
        Returns:
            list: list of project objects
        '''
        if projects == []:
            raise AssignmentException("Project list is Empty")
        
        temp = []
        for project in projects:
            try:
                status = Project.validate_project_data(project)
                if status == True:
                   temp.append(project)
            except AssignmentException as e:
                print(e)
                
        projects = temp
        
        project_list = []
        #sort list by priority
        index1 = 0
        size = len(projects)
        while index1 < size:
            
            index2 = 0
            while index2 < size-index1-1:
                if projects[index2]['priority'] > projects[index2+1]['priority']:
                    temp = projects[index2]
                    projects[index2] = projects[index2+1]
                    projects[index2+1] = temp
                index2 += 1
            index1 += 1
        
        #convert project dict to objects 
        for project in projects:
            project_list.append(Project(project['id'],project['numPeopleRequired'],project['requiredSkills'],project['priority']))
        
        return project_list
    
    def assign_employee(self, employees: list, projects: list):
        '''
        Assignes employees to poject
        
        Args:
            employees (list): list of employees
            projects (list): list of projects
            
        Returns: dictionary of employees assigned to projects
        '''
        self.__emp_list = self.convert_employee_list_to_object(employees)
        self.__project_list = self.sort_and_convert_project_list_to_objects(projects)
            
        assignment = {}
        
        #going through every project
        for project in self.__project_list:
            emp_requirement = project.get_required_num_of_people()
            skill_requirement = project.get_required_skills()
            
            emps = []
            emp_ids = []
            #check and add employees if they have skills required
            for skill in skill_requirement[::-1]:
                for employee in self.__emp_list:
                    if emp_requirement <= 0:
                        break
            
                    if skill in employee.get_skills() and employee.is_available() and employee not in emps:
                        emps.append(employee)
                        emp_ids.append(employee.get_id())
                        emp_requirement -= 1
                        break
                    
                if emp_requirement == 0:
                    project.assign_employees(emps)
                    assignment[f'{project.get_id()}'] = emp_ids
                
        return assignment
    
    def find_unassined_employees(self) -> list:
        '''
        finds unassined employees and returns in list
        
        returns:
            list: list of unassigned employee
        '''
        for employee in self.__emp_list:
            if employee.is_available():
                self.__unassigned_emp.append(employee.get_id())
        
        return self.__unassigned_emp
    
    def find_unstaffed_projects(self) -> list:
        '''
        finds unstaffed projects and returns in list
        
        Returns:
            list: list of unstaffed projects
        '''
        for project in self.__project_list:
            if not project.is_staffed():
                self.__unstaffed_projects.append(project.get_id())
                
        return self.__unstaffed_projects
      
    def get_employee_project_assignment(self, employees: list, projects: list) -> dict:
        '''
        Gets employee project assignment details
        
        Args:
            employees (list): list of employees
            projects (list): list of projects
        Returns:
            dict: dictionari of project assignment report
        '''
        try:
            self.__project_assignment['projectAssignments'] = self.assign_employee(employees, projects)
            self.__project_assignment['unassignedEmployees'] = self.find_unassined_employees()
            self.__project_assignment['unstaffedProjects'] = self.find_unstaffed_projects()
        except AssignmentException as e:
            print(e)
            
        return self.__project_assignment
     
        
def main():           
    employees = [
    { 'id': "E1", 'skills': ["Python", "Django"], 'available': True },
    { 'id': "E2", 'skills': ["React"], 'available': True },
    { 'id': "E3", 'skills': ["Django"], 'available': True },
    { 'id': "E4", 'skills': ["Java", "Spring"], 'available': True },
    { 'id': "E5", 'skills': ["Java"], 'available': True },
    { 'id': "E6", 'skills': ["Python"], 'available': False }
    ]   

    projects = [
    {
        'id': "P1",
        'requiredSkills': ["Python", "Django"],
        'numPeopleRequired': 2,
        'priority': 1
    },
    {
        'id': "P2",
        'requiredSkills': ["Java", "Spring"],
        'numPeopleRequired': 2,
        'priority': 2
    },
    {
        'id': "P3",
        'requiredSkills': ["React", "NodeJS"],
        'numPeopleRequired': 2,
        'priority': 3
    }
    ] 

    allocate = AllocateEmployee()
    temp = allocate.get_employee_project_assignment(employees, projects)
    print(json.dumps(temp, indent=4))
    
if __name__ == '__main__':
    main()
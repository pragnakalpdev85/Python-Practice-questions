# Question 5: Simple Gym Workout Tracker

# Problem Statement
# Design and implement a console-based Gym Workout Tracker using Object-Oriented Programming.
# Members visit the gym and perform exercises. 

# Each exercise has:
# Name (e.g., Bench Press, Squats)
# Sets completed
# Reps per set
# Weight used (in kg)
# The System Calculates
# Total volume for an exercise = sets × reps × weight

# Calories burned for the workout
# (Simple formula: 6 calories per minute, and each set takes approx. 2 minutes)
# Feedback Based on Total Volume
# ≥ 5000 kg → "Great workout!"
# 2000–5000 kg → "Good effort!"
# < 2000 kg → "Keep pushing!"

# Features
# Add a member (name and member ID)
# Start a new workout session for a member
# Add exercises to the current workout
# View workout summary with total volume, calories burned, and feedback
# List all members

# Sample Input & Expected Output
# === Gym Workout Tracker ===
# 1. Add Member
# 2. Start Workout
# 3. Add Exercise to Workout
# 4. View Workout Summary
# 5. List All Members
# 6. Exit
# Enter choice: 1
# Enter Member ID: M001
# Enter Name: Rohan Sharma
# Member added.

# Enter choice: 2
# Enter Member ID: M001
# Workout session started for Rohan Sharma.

# Enter choice: 3
# Enter Exercise Name: Bench Press
# Enter Sets: 4
# Enter Reps per set: 10
# Enter Weight (kg): 60
# Exercise added!

# Enter choice: 3
# Enter Exercise Name: Squats
# Enter Sets: 3
# Enter Reps per set: 12
# Enter Weight (kg): 80
# Exercise added!

# Enter choice: 4
# Enter Member ID: M001

# === Workout Summary for Rohan Sharma ===
# Exercise         | Sets | Reps | Weight | Volume
# Bench Press      | 4    | 10   | 60kg   | 2400kg
# Squats           | 3    | 12   | 80kg   | 2880kg
# ------------------------------------------------
# Total Volume     : 5280kg
# Estimated Calories Burned: 84
# Feedback         : Great workout!

# Enter choice: 5

# === All Members ===
# [M001] Rohan Sharma -->

class Exercise:
    '''
    Represent Exercise like squat, bench press etc.
    
    This class provides functionalities like calculate volume and
    calculate calories.
    
    Attributes:
        name (str): name of the exercise
        sets (int): sets of the exercise
        reps (int): total reps in one set
        weight_used (float): weight used for exercise (in kg)
    '''
    
    def __init__(self, name: str, sets: int, reps: int, weight_used: float):
        '''
        Initialize the exercise object
        
        Args:
            name (str): name of the exercise
            sets (int): sets of the exercise
            reps (int): total reps in one set
            weight_used (float): weight used for exercise (in kg)
        '''
        self.__name = name
        self.__sets = sets
        self.__reps = reps
        self.__weight_used = weight_used
        
    def get_name(self):
        '''
        gets name of the exercise
        
        Returns:
            str: name of the exercise
        '''
        return self.__name
        
    def get_sets(self):
        '''
        gets sets of the exercise
        
        Returns:
           int: sets of the exercise
        '''
        return self.__sets
        
    def get_reps(self):
        '''
        gets reps of the exercise
        
        Returns:
            int:reps of the exercise
        '''
        return self.__reps

    def get_weight(self):
        '''
        gets weight used in the exercise
        
        Returns:
            float :weight used in the exercise
        '''
        return self.__weight_used
        
    def calculate_volume(self) -> float:
        '''
        Calculates volume of exercise performed
        
        Returns:
            float: Volume of exercise performed
        '''
        return self.__sets * self.__reps * self.__weight_used
    
    def calculate_calories(self) -> float:
        '''
        Calculates calories burned in exercise
        
        Returns:
            float: calories burned by performing exercise
        '''
        return self.__sets * 12
    

class Member:
    '''
    Represents member of gym
    
    This class provides functionalities like view workout summery, add workout,
    list members of the gym, start workout, search member
    
    class attributes:
        list_members (list): list of all members
    instance Attributes:
        id (str): id of the gym member
        name (str): name of the member
        list_exercise (list): list of exercise members perform
    '''
    list_members = []
    
    def __init__(self, id: str, name: str, list_exercise = []):
        '''
        Initialize the member object
        
        Args:
            id (str): id of the gym member
            name (str): name of the member
            list_exercise (list): list of exercise members perform
        '''
        self.__id = id
        self.__name = name
        self.__session_active = False
        self.__list_exercise = list_exercise
        Member.list_members.append(self)
    
    def get_id(self) -> str:
        '''
        Gets id of the member
        
        Returns:
            str: id of the member
        '''   
        return self.__id
    
    def get_name(self) -> str:
        '''
        Gets name of the member
        
        Returns:
            str: name of the employee
        '''
        return self.__name
    
    def start_workout(self) -> str:
        '''
        starts workout session of member
        
        Returns:
            str: success Message
        '''
        if self.__session_active:
            return "Workout session is already started"
        else:
            self.__list_exercise = []
            self.__session_active = True
            return f"Workout session started for {self.__name}."
    
    def add_exercise(self, exercise: Exercise) -> str:
        '''
        Addes exercise to member's workout session
        
        Args:
            exercise (Exercise): object of Exercise class
        Returns:
            str: success message
        '''
        self.__list_exercise.append(exercise)
        return "Exercise added!"
    
    def view_workout_summary(self) -> str:
        '''
        Gets Workout summary of the member
        
        Returns:
            str: workout summery of member
        '''
        if self.__list_exercise == []:
            return f"No exercise is performed by {self.__name}"
        
        output = f'=== Workout Summary for {self.__name} ===\n'
        output += "Exercise          | Sets | Reps | Weight | Volume\n"
        space = "                 "
        
        total_cal = 0
        total_volume = 0
        for exercise in self.__list_exercise:
            output += exercise.get_name()+ space[len(exercise.get_name())-1:] + '|'
            
            sets = f" {exercise.get_sets()}"
            output += f'{sets}' + space[len(sets):6] + '|'
            
            reps = f" {exercise.get_reps()}"
            output += f'{reps}' + space[len(reps):6] + '|'
            
            weight = f' {exercise.get_weight()}Kg'
            output += f'{weight}'+ space[len(weight):8] + '|'
            
            volume = exercise.calculate_volume()
            output += f' {volume}Kg'
            output += '\n'
            
            total_cal += exercise.calculate_calories()
            total_volume += volume
            
        output += "-----------------------------------------------------\n"
        output += f"Total Volume     : {total_volume}Kg\n"
        output += f"Estimated Calories Burned: {total_cal}\n"
        output += "Feedback         :"
        if total_volume >= 5000:
            output += "Great workout!"
        elif total_volume < 5000 and total_volume >= 2000:
            output += "Good effort!"
        else:
            output += "Keep pushing!"
        
        return output            
            
    @classmethod
    def search_member(cls, id: str):
        '''
        Searches member in gym members
        
        Args:
            id (str): id of the member
        Returns:
            Member: object of member class
        '''
        temp_list = cls.list_members
        
        for member in temp_list:
            if member.get_id() == id:
                return member
            
        return None
    
    @classmethod
    def list_all_members(cls) -> str:
        '''
        lists all members of the gym
        
        Returns:
            str: data of all members of the gym
        '''
        if cls.list_members == []:
            return ''
        
        output = "======All Members======"
        for member in cls.list_members:
            output += f"\n[{member.get_id()}]  {member.get_name()}"
            
        return output
 
   
class InputValidate:
    '''
    Represents validation class
    '''
    
    @staticmethod
    def input_choice() -> int:
        '''
        validates input choice

        Returns:
            int: choice of user
        '''
        while True:
            try:
                choice = int(input("Enter your choice (1-6):"))
                if choice > 6 or choice < 1:
                    raise ValueError()
                return choice
            except ValueError as e:
                print("Invalid choice, Enter your choice (1-6) Again")
            
    @staticmethod  
    def input_str(name: str) -> str:
        '''
        takes input of string
        
        Returns:
            str: string value
        '''  
        while True:
            value = input(f"Enter {name}: ")
            if value == '':
                print("There is no value in input.")
                continue
            return value
      
    @staticmethod  
    def input_sets_reps(msg: str) -> int:
        '''
        takes input of sets or reps
        
        returns:
            int: number of reps of set
        '''        
        while True:
            try:
                value = int(input(f"Enter {msg}: "))
                if value <= 0:
                    raise ValueError()
                return value
            except ValueError as e:
                print(f"Invalid input of {msg}, Enter again")

    @staticmethod
    def input_weight() -> float:
        '''
        takes weight as input
        
        returns:
            float: weight used in exercise
        '''
        while True:
            try:
                value = float(input(f"Enter Weight (Kg): "))
                if value <= 0:
                    raise ValueError()
                return value
            except ValueError as e:
                print(f"Invalid input of weight, Enter again")
        
        
def main():
    active_member = None
    
    while True:
        print("\n====== Gym Workout Tracker ======")
        print("1. Add Member")
        print("2. Start Workout")
        print("3. Add Exercise to Workout")
        print("4. View Workout Summary")
        print("5. List All Members")
        print("6. Exit\n")
        choice = InputValidate.input_choice()
        
        match choice:
            case 1:
                id = InputValidate.input_str("Id")
                name = InputValidate.input_str("Name")
                
                present = Member.search_member(id)
                if present == None:
                    Member(id, name)
                    print("Member is Added")
                else:
                    print(f"Member with Id {id} is already prsent, Enter new Id")

            case 2:
                id = InputValidate.input_str("Member Id")
                active_member = Member.search_member(id)
                if active_member != None:
                    res = active_member.start_workout()
                    print(res)
                else:
                    print(f"There is no Member with Id {id}")
                    
            case 3:
                if active_member == None:
                    print("No Member has started a workout yet.")
                    continue
                
                name = InputValidate.input_str("Exercise name")
                sets = InputValidate.input_sets_reps("Sets")
                reps = InputValidate.input_sets_reps("Reps per set")
                weight = InputValidate.input_weight()
                
                exercise = Exercise(name, sets, reps, weight)
                
                active_member.add_exercise(exercise)
                print("Exercise added!")
                
            case 4:
                id = InputValidate.input_str("Member Id")
                search = Member.search_member(id)
                if search != None:
                    res = search.view_workout_summary()
                    print(res)
                else:
                    print(f"There is no Member with Id {id}")
                
            case 5:
                result = Member.list_all_members()
                if result == '':
                    result = "There are no Members registered"
                print(result)
            case 6:
                break
        
if __name__ == '__main__':
    main()
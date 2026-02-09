# Question 3: Electricity Bill Calculator
# Problem Statement
# Design and implement a console-based Electricity Bill Calculator using Object-Oriented Programming.
# A power company charges customers based on units consumed in a month with the following slab rates.

# Slab Rates
# 0 – 100 units: ₹5.00 per unit
# 101 – 200 units: ₹7.00 per unit
# 201 – 300 units: ₹9.00 per unit
# Above 300 units: ₹12.00 per unit

# Additional Rules (Logical Part)
# If a customer consumes more than 400 units, a 10% surcharge is added on the total bill.
# Senior citizens (age ≥ 60) get a flat 15% discount on the final bill (after surcharge, if any).
# Fixed meter charge: ₹150 (added to every bill).

# The System Should
# Add a customer (with customer ID, name, age)
# Record units consumed in a month
# Calculate and display the electricity bill with full breakdown
# List all customers

# Sample Input & Expected Output
# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 1
# Enter Customer ID: C001
# Enter Customer Name: Rajesh Kumar
# Enter Age: 45
# Customer 'Rajesh Kumar' (ID: C001) added successfully.

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 1
# Enter Customer ID: C002
# Enter Customer Name: Meera Devi
# Enter Age: 62
# Customer 'Meera Devi' (ID: C002) added successfully.

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 1
# Enter Customer ID: C003
# Enter Customer Name: Umang Patel
# Enter Age: 28
# Customer 'Umang Patel' (ID: C003) added successfully.

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 2
# Enter Customer ID: C001
# Enter Units Consumed this month: 350
# Units (350) recorded for customer C001.

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 2
# Enter Customer ID: C002
# Enter Units Consumed this month: 150
# Units (150) recorded for customer C002.

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 2
# Enter Customer ID: C003
# Enter Units Consumed this month: 450
# Units (450) recorded for customer C003.

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 3
# Enter Customer ID: C001

# ==================================================
# ELECTRICITY BILL
# Customer ID : C001
# Name        : Rajesh Kumar
# Age         : 45 
# Units Consumed: 350
# --------------------------------------------------
# 0-100 units: 100 × ₹5.00 = ₹500.00
# 101-200 units: 100 × ₹7.00 = ₹700.00
# 201-300 units: 100 × ₹9.00 = ₹900.00
# Above 300 units: 50 × ₹12.00 = ₹600.00

# Base Amount: ₹2700.00
# Fixed Meter Charge: ₹150.00
# Subtotal: ₹2850.00

# Final Total Bill: ₹2850.0
# ==================================================

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 3
# Enter Customer ID: C002

# ==================================================
# ELECTRICITY BILL
# Customer ID : C002
# Name        : Meera Devi
# Age         : 62 (Senior Citizen)
# Units Consumed: 150
# --------------------------------------------------
# 0-100 units: 100 × ₹5.00 = ₹500.00
# 101-200 units: 50 × ₹7.00 = ₹350.00

# Base Amount: ₹850.00
# Fixed Meter Charge: ₹150.00
# Subtotal: ₹1000.00
# 15% Senior Citizen Discount: -₹150.00

# Final Total Bill: ₹850.0
# ==================================================

# === Electricity Bill Calculator Menu ===
# 1. Add New Customer
# 2. Record Units Consumed
# 3. Calculate & Display Bill
# 4. List All Customers
# 5. Exit

# Enter your choice (1-5): 3
# Enter Customer ID: C003

# ==================================================
# ELECTRICITY BILL
# Customer ID : C003
# Name        : Umang Patel
# Age         : 28 
# Units Consumed: 450
# --------------------------------------------------
# 0-100 units: 100 × ₹5.00 = ₹500.00
# 101-200 units: 100 × ₹7.00 = ₹700.00
# 201-300 units: 100 × ₹9.00 = ₹900.00
# Above 300 units: 150 × ₹12.00 = ₹1800.00

# Base Amount: ₹3900.00
# Fixed Meter Charge: ₹150.00
# Subtotal: ₹4050.00
# 10% Surcharge (units > 400): +₹405.00

# Final Total Bill: ₹4455.0
# ==================================================

class Customer:
    '''
    Represents customer
    
    This class provides functionalities like display all customers, display bill of the customer,
    list all customers, add new consumer and record unit
    
    Class Attributes:
        customer_list (list): list of all consumers
        total_unit_consumed (float): total unit consumed
    
    Instance Attributes:
        cust_id (str): id of the customer
        name (str): name of the customer
        age (int): age of the customer
        unit_consumed (float): unit consumed by consumer
    '''
    
    customer_list = []
    
    def __init__(self, cust_id: str, name: str, age: int, unit_consumed = 0):
        '''
        Initialize customer objects
        
        Args:
            cust_id (str): id of the customer
            name (str): name of the customer
            age (int): age of the customer
            unit_consumed (float): unit consumed by consumer
        '''
        self.__cust_id = cust_id
        self.__name = name
        self.__age = age
        self.__unit_consumed = unit_consumed
        self.customer_list.append(self)
        
    def get_cust_id(self) -> str:
        '''
        Gets customer Id
        
        Returns:
            str: id of the customer
        '''
        return self.__cust_id
    
    def get_unit_consumed(self) -> float:
        '''
        Gets customer's unit consuption
        
        Returns:
            float: unit consumed by customer
        '''
        return self.__unit_consumed
        
    def get_age(self) -> int:
        '''
        Gets age of Customer
        
        Returns:
            int: age of customer
        '''
        return self.__age
    
    def get_name(self) -> str:
        '''
        Gets name of customer
        
        Returns:
            str: name of the customer
        '''
        return self.__name
    
    def set_unit_consuption(self, unit: float):
        '''
        sets unit_consumed
        
        Args:
            unit (float): unit consumed
        '''
        self.__unit_consumed = unit
        
    @staticmethod    
    def search_customer(cust_id: str):
        '''
        searches customer from customer id
        
        Args:
            cust_id (str): id of the customer
        Returns:
            Customer: object of Customer
        '''
        for customer in Customer.customer_list:
            if cust_id == customer.get_cust_id():
                return customer
        return None
    
    @staticmethod
    def record_unit(cust_id: str, unit: float) -> str:
        '''
        record unit consuption of user
        
        Args:
            cust_id (str): id of the customer
            unit (float): unit consumed by customer
        Returns:
            str: message
        '''
        customer = Customer.search_customer(cust_id)
        customer.set_unit_consuption(unit)
        return f"Units ({unit}) recorded for customer {cust_id}."
    
    @staticmethod
    def calculate_bill(cust_id):
        '''
        calculates customer bill
        
        Args:
            cust_id (str): id of the customer
        Returns:
            str: bill of the consumer
        '''
        bill_total = 0
        customer = Customer.search_customer(cust_id)
        units = customer.get_unit_consumed()
        age = customer.get_age()
        
        bill = '==================================================\n'
        
        bill += f"Customer ID : {customer.get_cust_id()}\nName        : {customer.get_name()}\n"
        
        if age >= 60:
            bill += f"Age         : {age} (Senior Citizen)\n"
        else:
            bill += f"Age         : {age}\n"
            
        bill += f"Units Consumed: {customer.get_unit_consumed()}\n"
        bill += "--------------------------------------------------\n"
        
        #calculating bill total
        if units <= 100:
            bill_total = units*5
            bill += f"0-100 units: {units} x ₹5.00 = ₹{units*5}\n"
            
        elif units > 100 and units <= 200:
            bill_total = (100*5) + (units-100)*7
            bill += f"0-100 units: 100 x ₹5.00 = ₹500.00\n"
            bill += f"101-200 units: {units - 100} x ₹7.00 = ₹{(units-100) * 7}\n"

        elif units > 200 and units <= 300:
            bill_total = (100*5) + (100*7) + (units-200)*9
            bill += f"0-100 units: 100 x ₹5.00 = ₹500.00\n"
            bill += f"101-200 units: 100 x ₹7.00 = ₹700.00\n"
            bill += f"201-300 units: {units - 200} x ₹9.00 = ₹{(units - 200)*9}\n"
        else:
            bill_total = (100*5) + (100*7) + (100*9) + (units-300)*12
            bill += f"0-100 units: 100 x ₹5.00 = ₹500.00\n"
            bill += f"101-200 units: 100 x ₹7.00 = ₹700.00\n"
            bill += f"201-300 units: 100 x ₹9.00 = ₹900.00\n"
            bill += f"Above 300 units: {units-300} x ₹12.00 = ₹{(units-300) * 12}\n"
            
        bill += f"\nBase Amount: {bill_total}\n"
        bill += f"Fixed Meter Charges: ₹150\n"
        bill_total += 150
        bill += f"Subtotal: {bill_total}\n"
        if units > 400:
            bill += f"10% Surcharge (units > 400): +{bill_total * 0.1}\n"
            bill_total += (bill_total*0.10)
            
        if age >= 60:
            bill += f"15% Senior Citizen Discount: -₹{bill_total*0.15}\n"
            bill_total -= (bill_total*0.15)
            
        bill += f"\nFinal bill total: {bill_total}\n"
        bill += f"=================================================="
        
        return bill
    
    @staticmethod
    def list_all_customers() -> str:
        list_cust = Customer.customer_list
        
        if list_cust == []:
            return ''
        
        ans = '==================================================\n'
        for customer in list_cust:
            ans += f"Customer ID : {customer.get_cust_id()}\n"
            ans += f"Name        : {customer.get_name()}\n"
            ans += f"Age         : {customer.get_age()}"
            if customer.get_age() >= 60:
                ans += "(Senior Citizen)"
            ans += "\n--------------------------------------------------\n"
            
        return ans
            
    @staticmethod
    def input_choice() -> int:
        '''
        validates input choice

        Returns:
            int: choice of user
        '''
        while True:
            try:
                choice = int(input("Enter your choice (1-5):"))
                if choice > 5 or choice < 1:
                    raise ValueError()
                return choice
            except ValueError as e:
                print("Invalid choice, Enter your choice (1-5) Again")
    
    @staticmethod
    def age_input_validation() -> int:
        '''
        validates input age

        Returns:
            int: age of customer
        '''
        while True:
            try:
                age = int(input("Enter Customer age: "))
                if age <= 0:
                    raise ValueError()
                return age
            except ValueError as e:
                print("Invalid Age, Enter Customer Age Again")
     
    @staticmethod 
    def unit_input_validation() -> float:
        '''
        validates unit consumtion input
        
        Returns:
            float: unit consuption of Customer
        '''
        while True:
            try:
                unit = float(input("Enter Units Consumed this month: "))
                if unit < 0:
                    raise ValueError()
                return unit
            except ValueError as e:
                print("Invalid unit input, Enter units consuption again")
 
    
def main():
    while True:
        print("\n=== Electricity Bill Calculator Menu ===")
        print("1. Add New Customer")
        print("2. Record Units Consumed")
        print("3. Calculate & Display Bill")
        print("4. List All Customers")
        print("5. Exit\n")
        choice = Customer.input_choice()
        
        match choice:
            case 1:
                id = input("Enter Customer ID: ")
                if Customer.search_customer(id) == None:
                    name = input("Enter Customer Name: ")
                    age = Customer.age_input_validation()
                    c = Customer(id, name, age)
                    print(f"Customer '{name}' (ID: {id}) added successfully.")
                else:
                    print(f"Customer with id {id} already exists please enter new id.")
                    
            case 2:
                id = input("Enter Customer ID: ")
                unit = Customer.unit_input_validation()
                res = Customer.search_customer(id)
                if res == None:
                    print(f"Customer with id {id} does not exists")
                else:
                    res = Customer.record_unit(id,unit)
                    print(res)
            case 3:
                id = input("Enter Customer ID: ")
                res = Customer.search_customer(id)
                if res == None:
                    print(f"Customer with id {id} does not exists")
                else:
                    res = Customer.calculate_bill(id)
                    print(res)
            case 4:
                ans = Customer.list_all_customers()
                if ans == '':
                    print("There are no customers.")
                else:
                    print(ans)
                print("==================================================")
            case 5:
                break
        
if __name__ == "__main__":
    main()
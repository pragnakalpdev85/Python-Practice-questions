# Question 4: Movie Ticket Booking System (Simple Version)

# Problem Statement
# Design and implement a console-based Movie Ticket Booking System using Object-Oriented Programming.
# A small cinema hall has only one screen with 50 seats arranged in 5 rows (A to E) and 10 seats per row (1 to 10).

# Ticket Prices
# Row A (Premium): ₹300
# Row B: ₹250
# Row C: ₹200
# Row D & E (Regular): ₹150

# Rules (Logical Part)
# Seats are initially all available.
# A customer can book multiple seats at once.
# Once booked, a seat cannot be booked again.
# Show total amount based on seat prices.
# Display seat layout (X = booked, O = available).

# The System Should
# Show current seat layout
# Book seats for a customer
# Calculate and display total ticket cost
# Show booking summary

# Sample Input & Expected Output
# === Movie Ticket Booking System ===
# 1. View Seat Layout
# 2. Book Tickets
# 3. Exit
# Enter choice: 1

# Current Seat Layout:
# Row A (₹300): O O O O O O O O O O
# Row B (₹250): O O O O O O O O O O
# Row C (₹200): O O O O O O O O O O
# Row D (₹150): O O O O O O O O O O
# Row E (₹150): O O O O O O O O O O

# Enter choice: 2
# Enter number of seats to book: 3
# Enter seat 1 (e.g., A5): A1
# Enter seat 2: B3
# Enter seat 3: C7
# Seats booked successfully!

# Booking Summary:
# A1 - ₹300
# B3 - ₹250
# C7 - ₹200
# Total Amount: ₹750

# Enter choice: 1

# Current Seat Layout:
# Row A (₹300): X O O O O O O O O O
# Row B (₹250): O O X O O O O O O O
# Row C (₹200): O O O O O O X O O O
# Row D (₹150): O O O O O O O O O O
# Row E (₹150): O O O O O O O O O O

class MovieHall:
    '''
    Represents cinema hall
    
    provides functionalities like bool tickets, show seats, check price etc
    
    Attributes:
        list_seat (list): list of seats
    '''
    
    def __init__(self):
        '''
        initilize movie hall objects
        
        args:
        list_seat (list): list of seats
        '''
        self.__list_seat = ['O' for seat in range(50)]
        
    def seatid_to_number(self, seat: str) -> int:
        '''
        converts seat id to number
        
        Args:
            seat (str): id of the seat
        Returns:
            int: seat number    
        '''
        rows = 'ABCDE'
        
        index = 0
        for row in rows:
            if row == seat[0]:
                break
            index += 1
            
        return index*10 + int(seat[1:]) - 1
        
    def isbooked(self,seat: str) -> bool:
        '''
        cheks if seat is booked or not
        
        Return:
            bool: booked status of seat
        '''
        
        return True if self.__list_seat[self.seatid_to_number(seat)] == 'X' else False
    
    def bookTicket(self, seat: str) -> bool:
        '''
        Books ticket
        
        Args:
            seat (str): seat id
        returns:
            bool: ticket booking success status
        '''
        seat_num = self.seatid_to_number(seat)
        if self.__list_seat[seat_num] == 'X':
            return False
        
        self.__list_seat[seat_num] = 'X'
        return True
    
    def display_seats(self) -> str:
        '''
        Displays all seats in cinema
        
        Returns:
            str: seating arrangement in cinema hall
        '''
        result = 'Current Seat Layout:\n'
        result += "Row A (₹300):"
        index = 0
        while index < 10:
            result += f" {self.__list_seat[index]}"
            index += 1
        result += "\nRow B (₹250):"
        while index < 20:
            result += f" {self.__list_seat[index]}"
            index += 1
        result += "\nRow C (₹200):"
        while index < 30:
            result += f" {self.__list_seat[index]}"
            index += 1
        result += "\nRow D (₹150):"
        while index < 40:
            result += f" {self.__list_seat[index]}"
            index += 1
        result += "\nRow E (₹150):"
        while index < 50:
            result += f" {self.__list_seat[index]}"
            index += 1
            
        return result

    def book_tickets(self, tickets: list) -> str:
        '''
        books multiple tickets
        
        Args:
            tickets (list): list of ticket ids
        str:
            str: success msg and ticket price total
        '''
        total_price = 0
        message = '\n'
        for ticket in tickets:
            if not self.isbooked(ticket):
                res = self.bookTicket(ticket)

                if ticket[0] == 'A':
                    total_price += 300
                    message += f"{ticket}: ₹300\n"
                elif ticket[0] == 'B':
                    total_price += 250
                    message += f"{ticket}: ₹250\n"
                elif ticket[0] == 'C':
                    total_price += 200
                    message += f"{ticket}: ₹200\n"
                else:
                    total_price += 150
                    message += f"{ticket}: ₹150\n"
            else:
                print(f"Ticket {ticket} is already Booked")
                
        message += f"Total Amount: ₹{total_price}"
        
        return message
    
    def seats_available(self) -> int:
        '''
        calculates how many seats are available
        
        Returns:
            int: number of seats available
        '''
        count = 0
        for seat in self.__list_seat:
            if seat == 'X':
                count += 1
                
        return 50-count
    
    @staticmethod
    def input_choice() -> int:
        '''
        validates input choice

        Returns:
            int: choice of user
        '''
        while True:
            try:
                choice = int(input("Enter your choice (1-3):"))
                if choice > 3 or choice < 1:
                    raise ValueError()
                return choice
            except ValueError as e:
                print("Invalid choice, Enter your choice (1-3) Again")    
        
    @staticmethod
    def input_and_validate_seat_id(num, list_seats) -> str:
        '''
        takes input and validate seat id
        
        Args:
            num (int): seat number
        Returns:
            str: id of the seat
        '''
        while True:
            try: 
                id = input(f"Enter seat {num}: ")
                rows = 'abcde'
                numbers = list('123456789') + ['10']
                if len(id) > 3 or id[0].lower() not in rows or id[1:] not in numbers:
                    raise ValueError("Invalid Seat id, Enter again")
                
                if id in list_seats:
                    print("Id is already entered. please Enter different seat id.")
                    continue
                
                return id.upper()
            
            except ValueError as e:
                print("Invalid Seat id, Enter again")

    @staticmethod
    def input_number_of_ticket():
        while True: 
            try:
                num = int(input("Enter number of seats you want to Book: "))
                if num > 50 and num < 0:
                    raise ValueError()
                return num
            except ValueError as e:
                print("Invalid Input of number of tickets, Enter again")


def main():
    moviehall = MovieHall()

    while True:
        print("\n=== Movie Ticket Booking System ===")
        print("1. View Seat Layout")
        print("2. Book Tickets")
        print("3. Exit\n")
        choice = MovieHall.input_choice()
        match choice:
            case 1:
                tickets = moviehall.display_seats()
                print(tickets)
            case 2:
                num = MovieHall.input_number_of_ticket()
                seats = moviehall.seats_available()
                if seats < num:
                    print(f"There are only {seats} seats available.")
                    continue
                    
                list_seats = []
                for nums in range(num):
                    id = MovieHall.input_and_validate_seat_id(nums+1, list_seats)
                    list_seats.append(id)
                message = moviehall.book_tickets(list_seats)
                print(message)
            case 3:
                break

if __name__ == "__main__":
    main()
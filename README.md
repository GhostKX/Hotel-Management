# Hotel Management System

A Python-based command-line hotel management system to manage room bookings. This system allows you to add, delete, and display customer details and their corresponding room numbers.

## Features

- **Customer Management**:  
  - Add new customers to the rooms.  
  - Delete existing customer records by their name and room number.  
  - Display all currently occupied rooms and their customers.  

- **Room Availability Check**:  
  - Prevent booking of rooms that are already occupied by displaying an appropriate message.  

- **User-Friendly Interface**:  
  - Easy-to-follow, interactive menu for managing hotel bookings.  

## Requirements

- **Python 3.x** or higher.  
- No external libraries required.  

## How to Run

1. Clone or download this repository to your local machine.  
2. Open your terminal or command prompt.  
3. Navigate to the directory where the script is located.  
4. Run the script with the following command:  

```bash
python main.py
```

## Usage

The system provides the following options for hotel room management:

- **Add**: Add a new customer and assign them to an available room.
- **Delete**: Remove a customer record by entering their name and room number.
- **Display**: View all the current customers and the rooms they are occupying.
- **Exit**: Exit the program.

## Example Usage
```
**************************************************
Welcome to the Hotel Management system!

To add new customer type in "Add".
To delete customer type in "Delete".
To see all customers type in "Display".
To leave type in "0".
::: Add

Customer name: John Doe
Room number: 101

Customer "John Doe" added to room number "101".
------------------------------------------------
Occupied rooms: 
------------------------------
Name: John Doe          Room: 101
------------------------------
Total number of occupied rooms: 1.

------------------------------------------------
```

## Code Structure 

- **Customer Data**: Customer details (name and room number) are stored in a dictionary, where the key is the customer's name and the value is the assigned room number.
- **Room Management:**: The system checks for room availability and ensures that no customer is assigned a room that's already occupied.

## Author

- Developed by **GhostKX**
- GitHub: **[GhostKX](https://github.com/GhostKX/Hotel-Management)**


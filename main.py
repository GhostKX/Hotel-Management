# Hotel Management system

# Dictionary for storing customer data
rooms = {}


# Logic for displaying all available customers
def display_customers():
    if len(rooms) == 0:
        print('\nOccupied rooms: None\n'
              f'All rooms are good to use!')
    elif len(rooms) != 0:
        count = 0
        print('\nOccupied rooms: ')
        print('-' * 30)
        for customer_name, customer_number in rooms.items():
            print(f'Name: {customer_name.capitalize()}          Room: {customer_number}')
            count += 1
        print('-' * 30)
        print('Total number of occupied rooms: {}.\n'.format(count))


# Logic for Deleting Customer Details
def delete_customers():
    display_customers()
    if len(rooms) == 0:
        print('\nNothing to delete!')
    elif len(rooms) != 0:
        delete_name = input('\nType in a name of the customer to delete: ')
        delete_number = int(input('\nType in a room number to delete: '))
        if delete_name in rooms.keys() and delete_number in rooms.values():
            rooms.pop(delete_name)
            print(f'\nCustomer "{delete_name}" successfully deleted')
        else:
            print('\nError invalid symbol!')


# Loop for calling the functions until user decides to stop using it
while True:
    print()
    print('*' * 50)
    print('Welcome to the Hotel Management system!')
    manager = input('\nTo add new customer type in "Add".\n'
                    'To delete customer type in "Delete".\n'
                    'To see all customers type in "Display".\n'
                    'To leave type in "0".\n'
                    '::: ').lower()
    if manager == 'add':

        #Logic for adding a new customer
        customer_name = input('\nCustomer name: ')
        customer_number = int(input('Room number: '))
        if customer_number in rooms.values() and customer_name in rooms.keys():
            print(f'\nRoom number "{customer_number}" is already occupied by "{customer_name}"!')
            print('Please choose another room.')
        elif customer_number not in rooms.values():
            rooms[customer_name.capitalize()] = customer_number
            print(f'\nCustomer "{customer_name.capitalize()}" added to room number "{customer_number}".')
            display_customers()
        else:
            print('\nError')

    elif manager == 'delete':

        # Calling the function to delete the customer
        delete_customers()

    elif manager == 'display':

        # Calling the function to display the customer
        display_customers()

    elif manager == '0':
        print('\nExit')
        break
    else:
        print('Error invalid symbol')

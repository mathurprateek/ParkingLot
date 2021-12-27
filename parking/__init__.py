from parking import parking_spot


# Options to perform Search for Vehicles(s)
def search_criteria():
    print("\n" + 'Please choose a Criteria for SEARCHING vehicle(s):')
    print('Enter "R" for "REGISTRATION NUMBER(s)"')
    print('Enter "V" for "VEHICLE TYPE"')
    print('Enter "C" for "COLOR"')
    print('Enter "M" for "MAKE"' + '\n')
    criteria = input('Your Criteria Choice: ').lower()
    if criteria in {'r', 'v', 'c', 'm'}:
        return criteria
    else:
        print('Incorrect input, please try again')
        return search_criteria()


# Operation triggers on parking slot
def select_action():
    print("\n" + 'Please choose your action')
    print('Enter "P" to "PARK" your vehicle')
    print('Enter "U" to "UN-PARK" your vehicle')
    print('Enter "S" for "STATUS" of Parking Lot')
    print('Enter "H" to "SEARCH" your vehicle(s)')
    print('Enter "Q" to "QUIT" Parking Lot Application' + "\n")
    choice = input('Your Choice: ').lower()
    if choice == 'p':
        parking_spot.park_check()
    elif choice == 'u':
        parking_spot.un_park(input("Please enter Registration Number of the vehicle: ").strip().lower())
    elif choice == 's':
        parking_spot.status()
    elif choice == 'h':
        parking_spot.search(search_criteria())
    elif choice == 'q':
        print("Thank You for Parking with us!")
    else:
        print('Incorrect input, please try again')
        select_action()

from parking.vehicle import Vehicle
from parking.parking_lot import ParkingLot


# Building Parking Slots and defining Entry Gates
def parking_lot_entry_slots_setup():
    try:
        print('Build your parking lot')
        lot_size = int(input('Enter TOTAL #SLOTS in parking area = ').strip().split()[0])
        entry_slots = set(map(int, (input('Mention Parking ENTRY GATE number(s) (space separated) = ')
                                    .strip()).split()))
        if lot_size > 1 and 1 <= max(entry_slots) <= lot_size:
            return ParkingLot(lot_size, entry_slots)
        else:
            print("\n" + "#SLOTS should be greater than 2" + "\n" +
                         "Entry Gate value(s) should be between 1 and #SLOTS " + "\n" + "Try Again!" + "\n")
            return parking_lot_entry_slots_setup()
    except IndexError:
        print("Check the value entered and Try Again!" + "\n")
        return parking_lot_entry_slots_setup()
    except ValueError:
        print("Check the value entered and Try Again!" + "\n")
        return parking_lot_entry_slots_setup()


# Parking lot object
parking_lot_obj = parking_lot_entry_slots_setup()

first_parking_lot = parking_lot_obj.parking_lot()
print(f' slot number : spot status =>  {first_parking_lot}')
updated_lot = first_parking_lot.copy()


# Validate and return value of Entry Gate
def get_entry_slot():
    try:
        e_slot = int(input("Please mention your Entry Gate: ").strip())
        if e_slot in parking_lot_obj.entries:
            return e_slot
        else:
            print("\n" + "Incorrect Entry Gate, Try again" + "\n")
            return get_entry_slot()
    except ValueError:
        print("\n" + "Check the Value of Entry Gate" + "\n")
        return get_entry_slot()


# Choose Action
def next_action():
    from parking import select_action
    select_action()


# Checking parking availability
def park_check():
    if 'vacant' not in updated_lot.values():
        print("Parking Full! No Vacant Slot")
        next_action()
    else:
        park()


# No result found for the Search parameters
def vehicle_not_found(c):
    if c == 0:
        print("NO VEHICLE(s) NOT FOUND! Check the details entered.")


# Vehicle Parking in slot
def park():
    print("Please enter details of Vehicle to be parked: ")
    reg_num = input("Registration Number* : ").strip()
    vehicle_type = input("Vehicle Type* (CAR / TRUCK / BUS): ").lower().strip()
    if len(reg_num) != 0 and len(vehicle_type) != 0 and vehicle_type in {'car', 'truck', 'bus'}:
        v = Vehicle(reg_num, vehicle_type)
        print(v)
        print("\n" + f"Parking Entry Gates: {parking_lot_obj.entries}" + "\n")
        entry_slot = get_entry_slot()
        for i in range(1, parking_lot_obj.slots+1):
            if entry_slot - i >= 1 and updated_lot[entry_slot - i] == 'vacant':
                updated_lot[entry_slot - i] = v
                print(f'Vehicle Parked at slot #{entry_slot - i} ')
                next_action()
                break
            elif entry_slot + i <= parking_lot_obj.slots and updated_lot[entry_slot + i] == 'vacant':
                updated_lot[entry_slot + i] = v
                print(f'Vehicle Parked at slot #{entry_slot + i} ')
                next_action()
                break
    else:
        print("\n" + "Check the value of 'Registration Number' AND 'Vehicle Type', Try Again!" + "\n")
        next_action()


# Un-Parking vehicle
def un_park(reg_num):
    for k, v in updated_lot.items():
        if type(v) != str and v.reg_num.lower() == reg_num:
            updated_lot[k] = 'vacant'
            print(f"Vehicle Un-Parked Successfully from slot #{k}")
            break
    else:
        print("WARNING: No Vehicle Found with the entered Registration Number, Try Again!")
    next_action()


# status of parking lot
def status():
    print("Status of Parking Lot: ")
    for k, v in updated_lot.items():
        print(f"Parking Slot #{k} >> {v}")
    next_action()


# search the parking lot as per reg. no.(s) / vehicle type / make / color
def search(criteria):
    # search and display vehicle(s) as per registration number(s) entered
    if criteria == 'r':
        r_nos = (input("Please enter REGISTRATION NUMBER(s) (space separated): ").strip().lower()).split()
        if len(r_nos) != 0:
            c = 0
            for k, v in updated_lot.items():
                if type(v) == str:
                    continue
                else:
                    for r_no in r_nos:
                        if v.reg_num.lower() == r_no:
                            print(f"Parking Slot #{k} >> {v}")
                            c += 1
            vehicle_not_found(c)
        else:
            print("No Value entered! Try Again.")
    # search and display vehicle(s) as per Vehicle Type entered
    elif criteria == 'v':
        v_type = (input("Please enter VEHICLE TYPE (CAR/TRUCK/BUS  any ONE): ").lower()).split()
        if len(v_type) != 0:
            c = 0
            for k, v in updated_lot.items():
                if type(v) != str and v.vehicle_type.lower() == v_type[0]:
                    print(f"Parking Slot #{k} >> {v}")
                    c += 1
            vehicle_not_found(c)
        else:
            print("No Value entered! Try Again.")
    # search and display vehicle(s) as per Color entered
    elif criteria == 'c':
        clr = (input("Please enter COLOR (Only ONE): ").lower()).split()
        if len(clr) != 0:
            c = 0
            for k, v in updated_lot.items():
                if type(v) != str and v.color.lower() == clr[0]:
                    print(f"Parking Slot #{k} >> {v}")
                    c += 1
            vehicle_not_found(c)
        else:
            print("No Value entered! Try Again.")
    # search and display vehicle(s) as per Make entered
    elif criteria == 'm':
        mk = (input("Please enter MAKE (Only ONE): ").lower()).split()
        if len(mk) != 0:
            c = 0
            for k, v in updated_lot.items():
                if type(v) != str and v.make.lower() == mk[0]:
                    print(f"Parking Slot #{k} >> {v}")
                    c += 1
            vehicle_not_found(c)
        else:
            print("No Value entered! Try Again.")
    next_action()

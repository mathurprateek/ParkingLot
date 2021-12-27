class ParkingLot:
    # method for initializing parking lot class
    def __init__(self, slot_num, entry_slots):
        print('\n' + 'Welcome to the linear parking lot application')
        print('Allowed Vehicle Type: Car / Truck / Bus  ONLY' + '\n')
        self.__slots = slot_num
        self.__entries = entry_slots

    # getter for slots
    @property
    def slots(self):
        return self.__slots

    # getter for entries
    @property
    def entries(self):
        return self.__entries

    # setting up parking lot for first time
    def parking_lot(self):
        lot = {k+1: 'vacant' for k in list(range(self.__slots))}
        for e in self.__entries:
            lot[e] = 'ENTRY GATE'
        return lot

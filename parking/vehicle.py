class Vehicle:
    # method for initializing Vehicle Class
    def __init__(self, reg_num, vehicle_type):
        self.__reg_num = reg_num
        self.__color = input("Color: ").strip()
        self.__make = input("Make: ").strip()
        self.__vehicle_type = vehicle_type

    # getter for registration number
    @property
    def reg_num(self):
        return self.__reg_num

    # getter for Color
    @property
    def color(self):
        return self.__color

    # getter for Make
    @property
    def make(self):
        return self.__make

    # getter for Vehicle Type
    @property
    def vehicle_type(self):
        return self.__vehicle_type

    # Representation of Vehicle's object
    def __repr__(self):
        return (f"Registration Number: {self.__reg_num}, "
                + f"Color: {self.__color}, "
                + f"Make: {self.__make}, "
                + f"Vehicle Type: {self.__vehicle_type}")

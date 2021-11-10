class Transport:

    def __init__(self, maker, model, year, speed):
        """Initializing the transport attributes"""
        self.maker = maker
        self.year = year
        self.speed = speed
        self.model = model
        self.odometer_reading = 0

    def description_name(self):
        """Returning the description of the transport"""
        desc = str(self.year) + ' ' + self.maker + ' ' + self.model + ' ' + str(self.speed)
        return desc.title()

    def read_odometer(self):
        """Displaying vehicle mileage"""
        print("Car mileage is " + str(self.odometer_reading) + " км")

    def update_odometer(self, km):
        """Updating odometer values"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Can't manually reduce the mileage")

    def increment_odometer(self, km):
        self.odometer_reading += km


class ElectricCar(Transport):

    def __init__(self, maker, model, year, speed):
        super().__init__(maker, model, year, speed)
        self.battery = 200

    def description_battery(self):
        print("This car has a battery with a capacity of " + str(self.battery) + " kilowatts")

    def description_name(self):
        """overriding parent method"""
        desc = str(self.year) + ' ' + self.model + ' ' + str(self.battery)
        return desc.title()


class DieselCar(Transport):

    def __init__(self, maker, model, year, speed):
        super().__init__(maker, model, year, speed)
        self.tank = 150

    def description_name(self):
        """overriding parent method"""
        desc = str(self.year) + ' ' + self.model + ' ' + str(self.tank)
        return desc.title()


class StationWagon(Transport):
    def __init__(self, maker, model, year, speed):
        super().__init__(maker, model, year, speed)

    def description_name(self):
        """overriding parent method"""
        desc = self.model
        return desc.title()

    @staticmethod
    def doors():
        small_car = 3
        big_car = 5
        ent = str(input("What is the size of the car?(small or big) "))
        if ent == "small":
            print("Car has ", small_car, " doors")
        elif ent == "big":
            print("Car has ", big_car, " doors")


class Carriage(Transport):
    def __init__(self, maker, model, year, speed):
        super().__init__(maker, model, year, speed)

    def description_name(self):
        """overriding parent method"""
        desc = str(self.year) + ' ' + self.model
        return desc.title()

    @staticmethod
    def lifting_capacity():
        s_power = 500
        m_power = 1000
        print("Car's power is : ", s_power)
        print("Car's power is : ", m_power)


class Pickup(DieselCar, ElectricCar, Carriage, StationWagon):

    def __init__(self, maker, model, year, speed):
        super().__init__(maker, model, year, speed)

    def description_name(self):
        """overriding parent method"""
        desc = str(self.year) + ' ' + self.model + ' ' + str(self.tank) + ' ' + str(self.battery)
        return desc.title()

    def lifting_capacity(self):
        s_power = 500
        m_power = 1000
        lif = str(input("What is the size of the car?(small or big) "))
        if lif == "small":
            print("Car's power is : ", s_power)
        elif lif == "big":
            print("Car's power is : ", m_power)

# car = ElectricCar("tesla", "S", 2019, 250)
# print(car.description_name())
# car.description_battery()


# pickup = Pickup("GT", "12wEE", 2005, 350)
# print(pickup.description_name())
# pickup.lifting_capacity()
# pickup.doors()



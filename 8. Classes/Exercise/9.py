# Battery Upgrade: Use the final version of electric_car.py from this section.Add a method to the Battery class called upgrade_battery(). This method should check the battery size and set the capacity to 85 if it isn’t already.Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. You should see an increase in the car’s range.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {str(self.battery_size)}-KWh battery.")

    def get_range(self):
        if self.battery_size <= 70:
            range = 240
        elif self.battery_size >= 85:
            range = 300

        message = f"This car can go approximately {str(range)} miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size < 85:
            print("\nBattery Upgraded Successfully")
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


tesla = ElectricCar("telsa", "model x", 2022)
tesla.battery.describe_battery()
# tesla.battery.battery_size = 85
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()

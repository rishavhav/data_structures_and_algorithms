# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    class Car:

        def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0

        def get_descriptive_name(self):
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()

        def read_odometer(self):
            print(f"This car has {self.odometer_reading} miles on it.")

        def update_odometer(self, mileage):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

        def increment_odometer(self, miles):
            self.odometer_reading += miles


    class ElectricCar(Car):
        def __init__(self, make, model, year, battery_size):
            super().__init__(make, model, year)
            self.battery_size = battery_size


    my_leaf = ElectricCar('nissan', 'leaf', 2024, '10000hz')
    print(my_leaf.get_descriptive_name())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

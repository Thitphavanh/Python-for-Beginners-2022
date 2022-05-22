class Car:
    brand = None
    year = None
    fuel = None
    status = None

    def __init__(self, brand='Tesla', year=2022, fuel=100.00, status=True):
        self.brand = brand
        self.year = year
        self.fuel = fuel
        self.status = status

    def checkStatus(self):
        if self.status == True:
            print('This car was pass checked')
        else:
            print('This car was not pass checked')

    def drive(self):
        print('This car is driving')


if __name__ == '__main__':
    car1 = Car('Lucid Air', 2021, 30.00, True)
    car2 = Car('Audi', 2022, 50.00, False)
    print(f'Brand : {car1.brand}')
    print(f'Menufacture year : {car1.year}')
    print(f'Fuel level : {car1.fuel}')

    car1.checkStatus()
    car1.drive()

    car2.checkStatus()
    car2.drive()

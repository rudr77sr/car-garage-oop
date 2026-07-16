import json

class Car:
    total_cars_created = 0

    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = mileage

        Car.total_cars_created += 1

    def drive(self, miles):
        self.mileage += miles

    def car_info(self):
        return str(self.year) + " " + self.brand + " " + self.model
    
    def __str__(self):
        return "{}".format(self.car_info())
    
    @property
    def mileage(self):
        return self._mileage
    
    @mileage.setter
    def mileage(self, miles):
        if miles < 0:
            raise ValueError("What? Why would you that? :(")
        self._mileage = miles

class ElecCar(Car):
    def __init__(self, brand, model, year, mileage, battery_range):
        super().__init__(brand, model, year, mileage)
        self.battery_range = battery_range

class Garage:
    def __init__(self):
        self.cars = []
 
    def add_car(self,car):
        self.cars.append(car)

    def find_car(self, brand):
        for car in self.cars:
            if car.brand.lower() == brand.lower():
                return car
        return None

    def print_all(self):
        for car in self.cars:
            print(car)

    def save_to_file(self, filename = "garage.json"):
        car_list = []
        for car in self.cars:
            car_data = {
                "brand": car.brand,
                "model": car.model,
                "year": car.year,
                "mileage": car.mileage
            }
            car_list.append(car_data)

        with open(filename, "w") as f:
            json.dump(car_list, f, indent=4)
    
    def load_from_file(self, filename = "garage.json"):
        with open(filename, "r") as f:
            car_list = json.load(f)

        for car_data in car_list:
            new_Car = Car(car_data["brand"], car_data["model"], car_data["year"], car_data["mileage"])
            self.cars.append(new_Car)

if __name__ == "__main__":
    garage = Garage()
    garage.add_car(Car("Toyota", "Corolla", 2020, 15000))
    garage.add_car(Car("Honda", "Civic", 2021, 8000))
    garage.print_all()

    garage.save_to_file()

    garage2 = Garage()
    garage2.load_from_file()
    print("\nLoaded from file:")
    garage2.print_all()
from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    price: int

    def get_price(self):
        return self.price
         

car_list = [
    Car(brand="Toyota", model="Corolla", year=2020, price=20000.0),
    Car(brand="Honda", model="Civic", year=2019, price=19000.0),
    Car(brand="Ford", model="Mustang", year=2022, price=35000.0),
    Car(brand="Tesla", model="Model 3", year=2023, price=45000.0),
    Car(brand="BMW", model="3 Series", year=2021, price=41000.0)
]

sorted_cars= sorted(car_list, key=Car.get_price)
for car in sorted_cars:
    print(car)
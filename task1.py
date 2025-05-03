from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    price: int


c = Car("Toyota", "Grandi", 2024, 25000000)
print(c)
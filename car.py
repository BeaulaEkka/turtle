from typing import Self


class Car:
    def __init__(self, brand: str, horse_power: int) -> None:
        self.brand = brand
        self.horse_power = horse_power

    def drive(self) -> None:
        print(f'{self.brand} is driving!')

    def get_info(self, var: int) -> None:
        print(var)
        print(f'{self.brand} with {self.horse_power} horsepower')

    def __str__(self) -> str:
        return f'{self.brand} with {self.horse_power} horsepower: string method'

    def __add__(self, other: Self) -> str:
        return f'{self.brand} + {other.brand} = {self.brand} & {other.brand}'


volvo: Car = Car('Volvo', 200)
bmw:Car=Car('bmw',300)
print(volvo + bmw)

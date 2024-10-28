class Car:
    def __init__(self, color: str, horse_power: int) -> None:
        self.color = color
        self.horse_power = horse_power


volvo: Car = Car('red', 200)
print(volvo.color)
print(volvo.horse_power)

mercedes:Car=Car('green',300)
print(mercedes.color)
print(mercedes.horse_power)

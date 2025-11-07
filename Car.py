class Car:
    def __init__(self, make, year_model):
        self._make = make
        self._year_model = year_model
        self._speed = 0
    def accelerate(self):
        self._speed += 5
    def decelerate(self):
        self._speed -= 5
    def get_speed(self):
        return self._speed
car1 = Car('Ford', ' 1968 Mustang')
while car1.get_speed() > 25:
    car1.accelerate()
    print(car1.get_speed())
while car1.get_speed() > 0:
    car1.decelerate()
    print(car1.get_speed())
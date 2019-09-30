class Car:
    def __init__ (self, speed, color, name, is_police, go, stop, turn):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.go = go
        self.stop = stop
        self.turn = turn

    def go(self):
        if self.go != 0:
            print('Машина поехала')

    def stop(self):
        if self.stop < 1:
            print('Машина остановилась')

    def turn(self):
        if self.turn == 1:
            print('Машина повернула налево')

    def turn(self):
        if self.turn == 2:
            print('Машина повернула направо')

class TownCar(Car):

    town_car = Car(0, 'yello', 'Prius', 'False', 0, 0, 1)

class SportCar(Car):

    sport_car = Car(220, 'red', 'Ferrari', 'False', 220, 220, 2)

class WorkCar(Car):

    work_car = Car(75, 'blue', 'Ford', 'False', 75, 75, 1)

class PoliceCar(Car):

    police_car = Car(160, 'black', 'Toyota', 'True', 160, 160, 1)





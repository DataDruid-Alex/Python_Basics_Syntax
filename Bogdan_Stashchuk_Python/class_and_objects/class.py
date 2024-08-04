class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car is stopped")


my_car = Car()
print(my_car)
print(isinstance(my_car, Car))
print(isinstance(my_car, str))
my_car.move()
my_car.stop()

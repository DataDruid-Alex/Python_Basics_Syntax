class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car is stopped")


my_car = Car()
print(my_car)
print(type(my_car))
print(isinstance(my_car, Car))
print(isinstance(my_car, object))
print()
print(dir(my_car))
print()
print(my_car.__dict__)

my_car.move()
my_car.stop()
my_car.move()
my_car.stop()
my_car.move()
my_car.stop()
my_car.move()
my_car.stop()

print("--------------")

my_second_car = Car()
print(my_car == my_second_car)
print(my_car is my_second_car)

Car.move(my_car)
# my_car.stop(my_car)
# TypeError: Car.stop() takes 1 positional argument but 2 were given

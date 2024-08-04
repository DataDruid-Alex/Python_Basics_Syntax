my_cars = ["BMW", "Mercedes"]
copied_cars = my_cars
copied_cars.append("Audi")
print(copied_cars)
print(my_cars)
print(id(my_cars) == id(copied_cars), id(my_cars))

def greeting(greet):
    return lambda name: f"{greet}, {name}!"


morning_greeting = greeting("Good Morning")
print(morning_greeting('Oleksandr'))
evening_greeting = greeting("Good Evening")
print(evening_greeting("Max"))


bye_greeting = greeting("Bye")
print(type(bye_greeting))
print(bye_greeting)
print(bye_greeting("Albert"))


def greet__(greet):
    def info(name):
        return f"{greet}, {name}!"
    return info


big_greet = greet__("Big greet")
b_g = big_greet("Locky")
print(b_g)

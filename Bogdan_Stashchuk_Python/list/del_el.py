user_inputs = [True, "hi", 343, 2.43]
print(user_inputs)
print(len(user_inputs))
print()

del user_inputs[1]
print(user_inputs, "changed user_inputs")
print(len(user_inputs))

print()
del user_inputs[-1]
print(user_inputs, "changed user_inputs")
print(len(user_inputs))
del user_inputs
print(user_inputs)

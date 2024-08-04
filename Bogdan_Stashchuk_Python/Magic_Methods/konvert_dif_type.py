# print('10'+5)
# TypeError: can only concatenate str (not "int") to str
# print(5+'10')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(5+int("10"))
int_num = 5
float_num = 4.5
print(int_num+float_num, "  int+float")
print(float_num+int_num, "  float+int")
bool_val = True
int_val = 7
print(bool_val+int_val, "True+7")
print(int_val+bool_val, "7+True")
print(False*24, "False*24")
print(24*False, "24*False")
print(int_num.__add__(float_num))
print(float_num.__radd__(int_num))

#################
print()
int_number = 50
float_number = 7.5
print(int_number*float_number)
print(int_number.__mul__(float_number))
# NotImplemented
print(int_number.__mul__("sds"))
# NotImplemented
print(float_number.__rmul__(int_number))
######################
print()
int_num = 50
str_val = 'avs'
print(int_num*str_val)
print()
print(str_val*int_num)
print(int_num.__mul__(str_val))
# NotImplemented
print()
print(str_val.__rmul__(int_num))

print()
print("      float")
##############
# float*str
print()
float_n = 5.4
str_value = "aqz"

print(float_n.__mul__(str_value))
# NotImplemented

print(str_value.__rmul__(float_n))
# TypeError: 'float' object cannot be interpreted as an integer

import sys
from array import array

# Ensure enough command-line arguments are provided
if len(sys.argv) < 3:
    raise IOError("You must provide a username and password")

# Extract command-line arguments
filename, username, password = sys.argv

# Print username and password to verify
print(username, password)

# Initialize an array to store username and password
# 'b' is the type code for signed char (1 byte per element)
user_log_data = array('b')
for char in (username + password):
    user_log_data.append(ord(char))

# Write the array to a binary file
with open("sys_my_argv_user.bin", 'wb') as my_user_file_log:
    user_log_data.tofile(my_user_file_log)

# Initialize an array for reading the data back
inport_log_data = array('b')

# Read the data back from the file
with open("sys_my_argv_user.bin", 'rb') as my_user_file_log:
    inport_log_data.fromfile(my_user_file_log, len(user_log_data))

# Convert the read array back to string
read_username_password = ''.join(chr(b) for b in inport_log_data)

# Print the read username and password to verify
print(read_username_password[:len(username)],
      read_username_password[len(username):])


# import sys
# from array import array
# print(sys.argv)
# # python Working_with_program_arguments_using_module_SYS.py test
# if len(sys.argv) < 3:
#     raise IOError("You must provide username and passwords")
# # username = sys.argv[1]
# # password = sys.argv[2]
# filename, username, password = sys.argv
# print(username, password)

# user_log_data = array('i', [])  # Create an empty integer array
# user_log_data.append((username, password))  # Append the tuple to the array

# inport_log_data = array('i', 0, 0)
# user_log_data.append((username, password))
# with open("sys_my_argv_user.bin", 'wb') as my_user_file_log:
#     user_log_data.tofile(my_user_file_log)
# with open("sys_my_argv_user.bin", 'rb') as my_user_file_log:
#     inport_log_data.fromfile(my_user_file_log, 2)

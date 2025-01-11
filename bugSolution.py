def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# Correct way to handle the return value of None
result = function_with_uncommon_error(10, 0)
if result is not None:
    print(result + 5)
else:
    print("Cannot perform calculation due to previous error")

# Declare the variable before using it.
undeclared_variable = 10
print(undeclared_variable)

#Correct use of mutable default arguments
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

list1 = append_to_list(1)
list2 = append_to_list(2)
print(list1) # Output: [1]
print(list2) # Output: [2]

#Correct use of global variables
my_global_var = 10
def modify_global():
    global my_global_var
    my_global_var = 20

modify_global()
print(my_global_var) # Output 20

def modify_global_correct():
    global my_global_var
    my_global_var = 30
modify_global_correct()
print(my_global_var) # Output 30

#Handle exceptions appropriately
try:
    file = open('nonexistent_file.txt', 'r')
except FileNotFoundError:
    print("Error: File not found")

# Correct way to handle variable scope
x = 10
def change_x():
    global x
    x = 20
    print(x)
change_x()
print(x) #Output 20

# Correct way to handle mutable objects
list_a = [1,2,3]
list_b = list_a.copy() #Create a copy to avoid unexpected side effects
list_b.append(4)
print(list_a) # Output [1,2,3]
print(list_b) # Output [1,2,3,4]
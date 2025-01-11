def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

# The uncommon error: ignoring the return value of None.
result = function_with_uncommon_error(10, 0)
print(result + 5)  # This will cause an error because result is None

# Another Uncommon error: Using a variable before it is defined.
print(undeclared_variable)

#Uncommon error: Incorrect use of mutable default arguments
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

list1 = append_to_list(1)
list2 = append_to_list(2)
print(list1) #Output: [1,2]
print(list2) #Output: [1,2] # Unexpected behavior

# Another uncommon error involving mutable default arguments
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

list3 = append_to_list(1)
list4 = append_to_list(2)
print(list3) #Output: [1]
print(list4) #Output: [2]  # Correct behavior

#Incorrect use of global variables
my_global_var = 10
def modify_global():
    global my_global_var
    my_global_var = 20

modify_global()
print(my_global_var) # Output 20

def modify_global_incorrect():
    my_global_var = 30
modify_global_incorrect()
print(my_global_var) # Output 20. Unexpected behavior. The global variable is not modified inside the function

#Uncommon error:  Ignoring exceptions
try:
    file = open('nonexistent_file.txt', 'r')
except FileNotFoundError:
    pass #This ignores the error, but it may not be the intended behavior. Better to handle exceptions appropriately.

# Uncommon error: Misunderstanding of variable scope
x = 10
def change_x():
    x = 20
    print(x) #Output 20
change_x()
print(x) #Output 10

#Example of a very subtle bug, a common error that's tricky to detect.
list_a = [1,2,3]
list_b = list_a
list_b.append(4)
print(list_a) # Output [1,2,3,4]
print(list_b) # Output [1,2,3,4] 
#Changing list_b also changes list_a because list_b points to the same list in memory. 
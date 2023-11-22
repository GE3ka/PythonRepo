# this is a single line comment
"""
This is
a multiline
comment
"""

my_new_favorite_language = 'Python' # variable declaration, initialize string

num1 = 42 #variable declaration, Data Types Numbers
num2 = 2.3 #variable declaration, Data Types Numbers
boolean = True #variable declaration, Data Types Boolean
string = 'Hello World' #variable declaration, initialize string, Data Types String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, Data Types List , initilize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}  #variable declaration, Data Types Dictionary initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, Data Types Tuples, initialize Tuples
print(type(fruit)) # log statement data type 
print(pizza_toppings[1]) # log statement second element of a list
pizza_toppings.append('Mushrooms') #List add value mushrooms
print(person['name']) #log statement value first element of list
person['name'] = 'George' #change value list first element 
person['eye_color'] = 'blue' # add value to list
print(fruit[2]) #log statement last element of tuples

if num1 > 45: #if statement 
    print("It's greater") # log statement
else: #if statement 
    print("It's lower") # log statement 

if len(string) < 5:  #if statement 
    print("It's a short word!") # log statement
elif len(string) > 15: #if statement 
    print("It's a long word!") # log statement
else: #if statement 
    print("Just right!") # log statement

for x in range(5): #for statement 
    print(x) #log statement
for x in range(2,5): #for statement
    print(x) #log statement
for x in range(2,10,3): #for statement 
    print(x) #log statement
x = 0 #variable declaration, intialize number
while(x < 5): #while statement
    print(x) # log staement
    x += 1 # add value

pizza_toppings.pop() # error: AttributeError: 'tuple' object has no attribute 'pop'
pizza_toppings.pop(1) # error: ttributeError: 'tuple' object has no attribute 'pop'

print(person) #log statement
person.pop('eye_color') #delete value
print(person) #log statement

for topping in pizza_toppings: #for statement 
    if topping == 'Pepperoni': #if statement
        continue # continue
    print('After 1st if statement')  #log statement
    if topping == 'Olives': #if statement 
        break  #break

def print_hello_ten_times(): #function definition
    for num in range(10): #for statement
        print('Hello') #log statement

print_hello_ten_times() #calling the function

def print_hello_x_times(x): #fucntion definition
    for num in range(x): # for statement
        print('Hello') #log statement

print_hello_x_times(4) #calling the function

def print_hello_x_or_ten_times(x = 10): #function definition
    for num in range(x): #for statement
        print('Hello') #log statement


print_hello_x_or_ten_times() #calling function where x = 10

print_hello_x_or_ten_times(4) #calling function where x=4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
num1 = 42  # variable declaration. Primitive, Numbers, Integer
num2 = 2.3  # variable declaration. Primitive, Numbers,Float
boolean = True  # variable declaration. Primitive, Boolean
string = 'Hello World'  # variable declaration. Primitive, String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  # variable declaration. Composite, List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37,'is_balding': False}  # variable declaration. Composite, Dictionary
# variable declaration. Composite, Tuple,
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))  # log statement, type check
print(pizza_toppings[1])  # log statement
pizza_toppings.append('Mushrooms')  # adding new element to list
print(person['name'])  # log statement
person['name'] = 'George'  # giving value for key, or rename
person['eye_color'] = 'blue'  # giving new key - value to the person dictionary
print(fruit[2])  # log statement

if num1 > 45:  # condition if
    print("It's greater")  # log statement
else:  # condition else
    print("It's lower")  # log statement

if len("string") < 5:  # condition if
    print("It's a short word!")  # not true, will skip this step
elif len("string") > 15:  # condition else if
    print("It's a long word!")  # not true, will skip this step
else:  # if every other condition skipped, will do the else statement
    print("Just right!")  # correct, this will be the output

for x in range(5):  # for loop from 0 until 5, 5 not included
    print(x)
for x in range(2, 5):  # for loop from 2 until 5: 2,3,4
    print(x)
for x in range(2, 10, 3):  # for loop from 2 until 10, every 3th : 2,5,8
    print(x)  # for x in range(start, stop, step)

x = 0  # while loop
while (x < 5): #condition
    print(x)
    x += 1 

pizza_toppings.pop()  # removing the last item
pizza_toppings.pop(1)  # removing the position 1 item

print(person)
person.pop('eye_color')  # remove key
print(person)

for topping in pizza_toppings:  # for loop start
    if topping == 'Pepperoni':
        continue  # continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #breaks the code, exiting out from the loop


def print_hello_ten_times():  # function
    for num in range(10):  # for loop
        print('Hello')


print_hello_ten_times()  # call the function = run


def print_hello_x_times(x):  # function with parameter x
    for num in range(x):
        print('Hello')


print_hello_x_times(4)  # call the function with argument 4


def print_hello_x_or_ten_times(x=10):  # function
    for num in range(x):
        print('Hello')


# calling function, with no argument we have x=10 will go 10 times
print_hello_x_or_ten_times()
# calling function with argument, we change how many time will run the for loop
print_hello_x_or_ten_times(4)

# multi line comment
"""
Bonus section # 
"""
# print(num3)  >>>NameError, num3 not defined
# num3 = 72
# fruit[0] = 'cranberry'  >>>TypeError, tuple does not support item assignment
# print(person['favorite_team'])  >>>KeyError: 'favorite_team'
# print(pizza_toppings[7])  >>>IndexError: list index out of range, only 4 objects are in Tuple no 7th to print
#   print(boolean)  >>>IndentationError: unexpected indent
# fruit.append('raspberry')  >>>AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) >> >AttributeError: 'tuple' object has no attribute 'pop'

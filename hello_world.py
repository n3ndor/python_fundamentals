# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Nandor"
print("Hello", name)  # with a comma
print("Hello" + name)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)  # with a comma
print("Hello" + str(name))  # with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sandwich"
fave_food2 = "steak"
print("I love to eat {} and {}.".format(
    fave_food1, fave_food2))  # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.")  # with an f string
#
print("I love to eat %s and %s." % (fave_food1, fave_food2))
print("I love to eat {0} and {1}.".format(fave_food1, fave_food2))
print("I love to eat {with_bread} and {without_bread}.".format(
    with_bread=fave_food1, without_bread=fave_food2))

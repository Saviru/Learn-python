''' Tutorial 1: Variables in Python '''


# Let's learn about variables in Python

# Python variables are containers for storing data values. Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it. It stores the data in memory location.

'''

There are some rules for naming a variable in Python :

1. A variable name must start with a letter or the underscore character.
2. A variable name cannot start with a number.
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
4. Variable names are case-sensitive (age, Age and AGE are three different variables).
5. The variable name should be meaningful and short.


'''

'''

We can use the assignment operator (=) to assign values to variables and we can use a unique name to identify the variable.

'''
# Examples :

x = 5
y = "Hello, World!"
num_array = [1, 2, 3, 4, 5]
flt = 3.14
num_tuple = (1, 2, 3, 4, 5)
stat = True

'''
These are some examples of variables. Here, x is an integer variable, y is a string variable, num_array is a list variable, flt is a float variable, num_tuple is a tuple variable and stat is a boolean variable.
I will explain about these data types in the next tutorials.

'''

# We can use the type() function to get the data type of the variable.

type(x)

'''

Here, the output will be <class 'int'> because x is an integer variable. But, we can't use the type() function to get the data type of the variable which is not defined. 
You can use the type() function without a variable by passing the value directly. For example, type(5) will return <class 'int'>.

'''
# Here are some more examples :

type(y) # <class 'str'>
type(num_array) # <class 'list'>
type(flt) # <class 'float'>
type(num_tuple) # <class 'tuple'>
type(stat) # <class 'bool'>

# We can also assign multiple values to multiple variables in a single line like this :

a, b, c = 5, 3.14, "Hello, World!"

# Here also, a is an integer variable, b is a float variable and c is a string variable and you can use these variables as other variables. There is no difference.

# We can also assign the same value to multiple variables in a single line like this :

d = e = f = "Hello, World!"

# Here, d, e and f are string variables and all of them have the same value "Hello, World!".

# We can update the value of the variable by assigning a new value to it.

g = 5

# Here, g is an integer variable and it has the value 5. Now, I will update the value of g.

g = 10

# Now, the value of g is 10.

# We can also delete the variable by using the del keyword.

del g

# Now, the variable g is deleted and you can't use it anymore.

# When you want to output the value of the variable, you can use the print() function.

print(x) # 5
print(y) # Hello, World!
print(num_array) # [1, 2, 3, 4, 5]
print(flt) # 3.14

# You can also use the print() function to output the value of the variable which is not defined.

print(5) # 5
print("Hello, World!") # Hello, World!

# You can also use the print() function to output the value of the variable which is deleted. But it gives an error.

print(g) # NameError: name 'g' is not defined








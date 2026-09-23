# What is the difference between input() and print() in Python?
input() reads user input and returns a string. print() creates an output to the console.

# What data type does the input() function return by default? How can you use it to get numeric input?
input() returns a string. For numeric inputs, convert it using a numeric datatype.
Example: int(input(...))

# Explain how formatted string literals (f-strings) improve readability in output statements. Give an example.
You can add variable and expressions inside of f-strings using curly brackets { } rather than using "string" + expression + "string".

## Less readable example:
```python
name = "Astrid"
age = 76
favourite_food = "cheese"

print(name + " is " + str(age) + " years old and loves " + favourite_food + ".")
```

## Much more readable example:
```python
name = "Astrid"
age = 76
favourite_food = "cheese"

print(f"{name} is {age} years old and loves {favourite_food}.")
```

# Can a variable change its data type during runtime in Python? Show an example.
```python
age = 13 #Age is currently an integer so we can do calculations with it
print(f"Your age in ten years is: {age+10}")

age = "Twenty-three" #Age changes datatype to a string, still the same variable
print(f"Your age in spelled format: {age}")
```

# What does it mean that Python is "dynamically typed"? How is that different from statically typed languages?
A statically typed language means that variable types are known at compile-time. The type is fixed/static and can be either explicitly specified or inferred.

A dynamically typed language means that variable types are known during run-time and doesn't require type specification. This makes it quicker to work with as a programmer.
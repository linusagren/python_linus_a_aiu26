>When is it better to use while statement and when is it better to use for statement

- **While**-loops is better when you don't know how many times you need to iterate.
- **For**-loops is better when you want to iterate through everything or a set amount.

>What is the difference between = and == in Python?

- **=** is value assignment.
- **==** is value comparison.

>Explain how an if-elif-else block works in Python. What happens if multiple conditions are true?
- if-blocks checks whether one or more conditions are true or false. If true, it runs the code block inside of it.
- elif is used for additional condition checks if the previous conditions are false.
- else-blocks runs if all previous conditions before are false.
- If multiple conditions are true, it will only run the first block that's true since it checks from top to bottom.

>What does the continue statement do in a loop? How is it different from break?

- **continue** skips the remaining parts of the current iteration and starts the next one.
- **break** exits out of the loop entirely.

>Explain the meaning of truthy and falsy values and give a few example of both

- **Truthy** values are values that Python treat as True when used as a condition, such as 5 and strings/lists with value(s).
- **Falsy** values are values that Python treat as False when used as a condition, such as 0, empty lists and empty strings.

```python
x = 1 #true
y = [] #false
```

>Can you nest control structures in Python (e.g., a loop inside an if)? Give a brief example.

```python
games = ["Old School RuneScape", "Project Zomboid", "Outlast 2"]
genres = ["MMORPG", "Zombie Survival", "Horror"]

print("Pick an option:")
print("A: Show all games")
print("B: Show all genres")
user_option = input().upper()

if user_option == "A":
    for game in games:
        print(game)
elif user_option == "B":
    for genre in genres:
        print(genre)
```

>Every expression can be part of a statement, but not all statements are expressions. True or false?

True. Expressions, for example 3 + 5 creates values that can be used in statements. However, some statements like if-statements aren't expressions because they don't create values. 
# Python Keywords

Python **keywords** are reserved words that have a special meaning in the Python language.

They are part of Python's syntax and cannot normally be used as variable names, function names, or class names.

For a beginner, it is important to know **what every keyword means and why it exists** before moving into advanced Python topics.

---

## Complete Python Keywords

### 1. `False`

Represents the Boolean value **false**.

**Importance:** Used whenever a condition or Boolean expression is false.

---

### 2. `None`

Represents the absence of a value.

**Importance:** Extremely important for handling missing, empty, or not-yet-assigned values.

---

### 3. `True`

Represents the Boolean value **true**.

**Importance:** Used whenever a condition or Boolean expression is true.

---

### 4. `and`

Combines multiple conditions where **all conditions must be true**.

**Importance:** Fundamental to Boolean logic and conditional programming.

---

### 5. `as`

Creates an alias or gives another name to something.

**Importance:** Commonly used with imports, exceptions, and context managers.

---

### 6. `assert`

Checks whether a condition is true.

**Importance:** Useful for detecting incorrect assumptions and validating program state during development.

---

### 7. `async`

Defines asynchronous code.

**Importance:** Essential for modern Python applications that perform many I/O operations concurrently, especially APIs and AI applications.

---

### 8. `await`

Waits for an asynchronous operation to complete.

**Importance:** One of the fundamental keywords for Python asynchronous programming.

---

### 9. `break`

Immediately stops the current loop.

**Importance:** Gives the programmer control over when a loop should terminate.

---

### 10. `case`

Defines an individual pattern inside a `match` statement.

**Importance:** Used for structural pattern matching.

---

### 11. `class`

Defines a class.

**Importance:** Fundamental to Python's object-oriented programming system.

---

### 12. `continue`

Skips the current loop iteration and moves to the next iteration.

**Importance:** Allows selective control over loop execution.

---

### 13. `def`

Defines a function.

**Importance:** One of the most important Python keywords because functions are the primary way to organize reusable code.

---

### 14. `del`

Deletes a reference, item, attribute, or variable binding.

**Importance:** Provides explicit control over removing references and objects from a program's namespace.

---

### 15. `elif`

Means **else if**.

**Importance:** Allows multiple conditions to be checked sequentially.

---

### 16. `else`

Defines what should happen when a previous condition is false or a loop completes without interruption.

**Importance:** Fundamental to conditional and loop control flow.

---

### 17. `except`

Defines how an exception should be handled.

**Importance:** Essential for writing programs that can handle errors safely.

---

### 18. `finally`

Defines code that should execute after exception handling regardless of whether an exception occurred.

**Importance:** Important for cleanup operations and resource management.

---

### 19. `for`

Creates a loop that iterates over items in an iterable.

**Importance:** One of the most commonly used keywords in Python for repetition and data processing.

---

### 20. `from`

Specifies what should be imported from a module or package.

**Importance:** Fundamental to Python's module and package system.

---

### 21. `global`

Declares that a variable belongs to the global scope.

**Importance:** Allows functions to explicitly work with variables defined in the global namespace.

---

### 22. `if`

Executes code conditionally.

**Importance:** One of the fundamental building blocks of programming and decision making.

---

### 23. `import`

Loads a module or package into a Python program.

**Importance:** Essential for using Python's standard library and third-party libraries.

---

### 24. `in`

Checks membership or is used when iterating over an iterable.

**Importance:** Fundamental for working with collections such as lists, strings, sets, dictionaries, and tuples.

---

### 25. `is`

Checks whether two references point to the same object.

**Importance:** Important for understanding Python object identity.

---

### 26. `lambda`

Creates a small anonymous function.

**Importance:** Provides a compact way to create simple functions.

---

### 27. `match`

Starts a structural pattern-matching statement.

**Importance:** Provides a modern way to compare a value against different patterns.

---

### 28. `nonlocal`

Refers to a variable in an enclosing function scope.

**Importance:** Important for understanding nested functions and Python's variable scope rules.

---

### 29. `not`

Reverses a Boolean condition.

**Importance:** Fundamental to Boolean logic.

---

### 30. `or`

Combines conditions where at least one condition must be true.

**Importance:** Fundamental to Boolean logic and conditional programming.

---

### 31. `pass`

Does nothing.

**Importance:** Provides a valid placeholder when Python requires a statement but no action is needed yet.

---

### 32. `raise`

Explicitly raises an exception.

**Importance:** Allows programmers to signal errors and enforce program rules.

---

### 33. `return`

Ends a function and optionally sends a value back to the caller.

**Importance:** Fundamental to functions and reusable Python code.

---

### 34. `try`

Starts an exception-handling block.

**Importance:** Allows Python programs to safely attempt operations that may produce errors.

---

### 35. `while`

Repeats code while a condition remains true.

**Importance:** Fundamental for condition-based loops.

---

### 36. `with`

Starts a context-management block.

**Importance:** Provides safe and automatic management of resources such as files, connections, and locks.

---

### 37. `yield`

Produces a value from a generator while preserving the generator's execution state.

**Importance:** Fundamental to Python generators and memory-efficient iteration.

---

# Python Soft Keywords

Python also has **soft keywords**.

Soft keywords have special meaning only in specific contexts. Unlike regular keywords, they can sometimes be used as identifiers.

The important soft keywords are:

---

## 38. `_`

The underscore can have special meaning in certain Python syntax contexts.

**Importance:** Used in several Python conventions and special syntax situations.

> `_` is not a regular Python keyword.

---

## 39. `case`

`case` is a soft keyword used inside `match` statements.

**Importance:** Defines a possible pattern in structural pattern matching.

---

## 40. `match`

`match` is used for structural pattern matching.

**Importance:** Provides pattern-based control flow.

---

## 41. `_`

Within pattern matching, `_` represents a wildcard pattern.

**Importance:** Allows a pattern to match anything.

---

# Complete Keyword List

For quick reference:

```text
False
None
True

and
as
assert
async
await

break
case
class
continue

def
del

elif
else
except

finally
for
from

global

if
import
in
is

lambda

match

nonlocal
not

or

pass

raise
return

try

while
with

yield
```

---

# Important Beginner Distinction

Not every important Python word is a keyword.

For example:

```text
print
len
range
type
list
dict
str
int
float
set
tuple
open
input
```

These are **built-in functions or built-in types**, not Python keywords.

For example:

```python
if len(numbers) > 0:
    print(numbers)
```

Here:

```text
if       → keyword
len      → built-in function
numbers  → variable
>        → operator
print    → built-in function
```

---

# Keywords vs Built-ins

| Keyword  | Built-in  |
| -------- | --------- |
| `if`     | `print()` |
| `for`    | `len()`   |
| `while`  | `range()` |
| `def`    | `type()`  |
| `class`  | `list()`  |
| `return` | `dict()`  |
| `import` | `str()`   |
| `try`    | `int()`   |
| `with`   | `open()`  |
| `async`  | `input()` |

---

# Important Note About `self`

`self` is **not a Python keyword**.

It is a conventional name used for the current object inside instance methods.

Similarly, these are not keywords:

```text
self
cls
args
kwargs
```

They are conventional names used by Python developers.

---

# Important Note About Python Versions

Python's keyword list can change as the language evolves.

You can always see the keywords available in your installed Python version using:

```python
import keyword

print(keyword.kwlist)
```

You can check whether a particular word is a keyword:

```python
keyword.iskeyword("def")
```

---

# Beginner Mastery Checklist

Before moving to the next Python topic, you should recognize these groups:

### Boolean

```text
True
False
None
```

### Conditions

```text
if
elif
else
```

### Loops

```text
for
while
break
continue
```

### Functions

```text
def
return
lambda
yield
```

### Classes

```text
class
```

### Exceptions

```text
try
except
else
finally
raise
assert
```

### Modules

```text
import
from
as
```

### Logic

```text
and
or
not
```

### Identity & Membership

```text
is
in
```

### Scope

```text
global
nonlocal
```

### Context Management

```text
with
```

### Asynchronous Programming

```text
async
await
```

### Pattern Matching

```text
match
case
```

### Other Important Keywords

```text
pass
del
```

---

# Key Takeaway

You **do not need to memorize every keyword immediately**.

The goal at the beginner stage is to:

1. Recognize every Python keyword.
2. Understand the basic meaning of each keyword.
3. Know which category each keyword belongs to.
4. Understand that keywords are part of Python's syntax.
5. Distinguish keywords from built-in functions and types.

Once you understand these keywords, you have the basic **vocabulary of Python** needed to move into variables, data types, control flow, functions, OOP, exceptions, modules, generators, decorators, and asynchronous programming.

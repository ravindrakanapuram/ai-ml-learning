# Chapter 1 — Python Fundamentals

A hands-on implementation of Python fundamentals required for AI/ML engineering.

This chapter focuses on writing clean, reusable, testable Python code rather than learning Python through theory alone.

---

## Overview

Python is the primary programming language used throughout modern AI/ML engineering.

Before working with:

* NumPy
* Pandas
* Scikit-learn
* PyTorch
* Transformers
* LLMs
* RAG
* AI Agents

it is important to have a strong understanding of Python fundamentals.

This chapter builds that foundation through executable examples, coding exercises, tests, and a practical ML-oriented project.

---

## Learning Objectives

By completing this chapter, I should be able to:

* Understand Python variables and data types.
* Work confidently with Python strings.
* Use lists, tuples, sets, and dictionaries.
* Write conditions and loops.
* Use comprehensions appropriately.
* Write clean and reusable functions.
* Understand function parameters.
* Use `*args` and `**kwargs`.
* Use lambda functions.
* Understand `map`, `filter`, and `reduce`.
* Handle exceptions correctly.
* Create and use modules.
* Create Python packages.
* Understand decorators.
* Implement iterators.
* Implement generators.
* Create and use context managers.
* Understand the basic Python execution model.
* Write testable Python code.
* Apply Python concepts to ML/AI-oriented problems.

---

# Concepts Covered

## 1. Variables and Data Types

Topics:

* Variable assignment
* Dynamic typing
* Integers
* Floats
* Complex numbers
* Booleans
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* `None`
* Type inspection
* Type conversion
* Mutability
* Immutability

Directory:

```text
01_variables_and_types/
├── variables.py
├── data_types.py
└── mutability.py
```

---

## 2. Strings

Topics:

* String creation
* Indexing
* Slicing
* String methods
* `strip`
* `split`
* `join`
* `replace`
* `lower`
* `upper`
* `startswith`
* Membership testing
* f-strings
* String normalization

Directory:

```text
02_strings/
└── strings.py
```

---

## 3. Data Structures

Topics:

### Lists

* Creating lists
* Indexing
* Slicing
* Adding elements
* Removing elements
* Sorting
* Iteration

### Tuples

* Immutable sequences
* Tuple unpacking
* Returning multiple values

### Sets

* Unique values
* Union
* Intersection
* Difference

### Dictionaries

* Key/value pairs
* Lookup
* Updating values
* Iteration
* Nested dictionaries

Directory:

```text
03_data_structures/
├── lists.py
├── tuples.py
├── sets.py
└── dictionaries.py
```

---

## 4. Control Flow

Topics:

* `if`
* `elif`
* `else`
* Nested conditions
* `for`
* `while`
* `break`
* `continue`
* `range`

Directory:

```text
04_control_flow/
├── conditions.py
├── for_loops.py
└── while_loops.py
```

---

## 5. Comprehensions

Topics:

* List comprehensions
* Dictionary comprehensions
* Set comprehensions
* Conditional comprehensions
* Nested comprehensions

Directory:

```text
05_comprehensions/
├── list_comprehensions.py
├── dict_comprehensions.py
└── set_comprehensions.py
```

The goal is to understand when comprehensions improve readability and when a normal loop is better.

---

## 6. Functions

Topics:

* Function definition
* Parameters
* Arguments
* Default parameters
* Keyword arguments
* Return values
* Multiple return values
* Type hints
* Docstrings
* Variable scope
* Local variables
* Global variables
* `*args`
* `**kwargs`

Directory:

```text
06_functions/
├── functions.py
├── parameters.py
├── args_kwargs.py
└── scope.py
```

The emphasis is on creating small, reusable functions suitable for production code.

---

## 7. Lambda and Functional Programming

Topics:

* Lambda functions
* `map`
* `filter`
* `reduce`
* When functional programming is useful
* When normal functions are preferable

Directory:

```text
07_lambda/
├── lambda_functions.py
├── map_examples.py
├── filter_examples.py
└── reduce_examples.py
```

---

## 8. Exceptions

Topics:

* `try`
* `except`
* `else`
* `finally`
* Built-in exceptions
* Raising exceptions
* Custom exceptions
* Input validation
* Error handling

Directory:

```text
08_exceptions/
├── exceptions.py
└── custom_exceptions.py
```

The goal is to write code that fails safely and provides meaningful errors.

---

## 9. Modules and Packages

Topics:

* Python modules
* Imports
* `__init__.py`
* Packages
* Reusable utilities
* Import organization
* `if __name__ == "__main__"`

Directory:

```text
09_modules_and_packages/
├── modules/
│   ├── __init__.py
│   ├── math_utils.py
│   └── text_utils.py
│
└── package_demo.py
```

---

## 10. Decorators

Topics:

* Functions as objects
* Nested functions
* Closures
* Decorators
* `functools.wraps`
* Practical decorators

Examples will demonstrate concepts relevant to real applications such as:

* Logging
* Timing
* Validation
* Authentication-style checks

Directory:

```text
10_decorators/
├── decorators.py
└── practical_decorators.py
```

---

## 11. Iterators

Topics:

* Iterable vs iterator
* `iter()`
* `next()`
* `StopIteration`
* Custom iterators
* Lazy iteration

Directory:

```text
11_iterators/
└── iterators.py
```

---

## 12. Generators

Topics:

* `yield`
* Generator functions
* Generator expressions
* Lazy evaluation
* Memory efficiency
* Streaming data

Directory:

```text
12_generators/
├── generators.py
└── data_generator.py
```

Generators will be connected to ML-style data processing where large datasets should not always be loaded into memory at once.

---

## 13. Context Managers

Topics:

* `with`
* Resource management
* `__enter__`
* `__exit__`
* Custom context managers
* `contextlib`

Directory:

```text
13_context_managers/
├── context_manager.py
└── custom_context_manager.py
```

---

## 14. Python Execution

Topics:

* Python source code
* Parsing
* Bytecode
* Python Virtual Machine
* Namespaces
* Scope
* Imports
* Module execution
* `__name__`
* `__main__`

Directory:

```text
14_python_execution/
└── execution_demo.py
```

The goal is to understand what happens when Python code is executed rather than treating Python as a black box.

---

# Repository Structure

```text
01-python-fundamentals/
│
├── README.md
├── requirements.txt
│
├── 01_variables_and_types/
│   ├── variables.py
│   ├── data_types.py
│   └── mutability.py
│
├── 02_strings/
│   └── strings.py
│
├── 03_data_structures/
│   ├── lists.py
│   ├── tuples.py
│   ├── sets.py
│   └── dictionaries.py
│
├── 04_control_flow/
│   ├── conditions.py
│   ├── for_loops.py
│   └── while_loops.py
│
├── 05_comprehensions/
│   ├── list_comprehensions.py
│   ├── dict_comprehensions.py
│   └── set_comprehensions.py
│
├── 06_functions/
│   ├── functions.py
│   ├── parameters.py
│   ├── args_kwargs.py
│   └── scope.py
│
├── 07_lambda/
│   ├── lambda_functions.py
│   ├── map_examples.py
│   ├── filter_examples.py
│   └── reduce_examples.py
│
├── 08_exceptions/
│   ├── exceptions.py
│   └── custom_exceptions.py
│
├── 09_modules_and_packages/
│   ├── modules/
│   └── package_demo.py
│
├── 10_decorators/
│   ├── decorators.py
│   └── practical_decorators.py
│
├── 11_iterators/
│   └── iterators.py
│
├── 12_generators/
│   ├── generators.py
│   └── data_generator.py
│
├── 13_context_managers/
│   ├── context_manager.py
│   └── custom_context_manager.py
│
├── 14_python_execution/
│   └── execution_demo.py
│
├── exercises/
├── solutions/
├── tests/
│
└── projects/
    └── ml_data_pipeline/
```

---

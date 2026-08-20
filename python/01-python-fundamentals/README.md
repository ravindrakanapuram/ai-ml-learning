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

# Daily Learning Plan

## Day 1 — Variables and Strings

Concepts:

* Variables
* Data types
* Type conversion
* Mutability
* Immutability
* Strings
* String methods
* f-strings

Commit:

```bash
git commit -m "feat: practice Python variables types and strings"
```

---

## Day 2 — Data Structures

Concepts:

* Lists
* Tuples
* Sets
* Dictionaries

Commit:

```bash
git commit -m "feat: add Python data structure examples"
```

---

## Day 3 — Control Flow

Concepts:

* Conditions
* `for`
* `while`
* `break`
* `continue`

Commit:

```bash
git commit -m "feat: practice Python control flow"
```

---

## Day 4 — Comprehensions

Concepts:

* List comprehensions
* Dictionary comprehensions
* Set comprehensions

Commit:

```bash
git commit -m "feat: implement Python comprehensions"
```

---

## Day 5 — Functions

Concepts:

* Functions
* Parameters
* Return values
* Type hints
* Scope
* `*args`
* `**kwargs`

Commit:

```bash
git commit -m "feat: implement reusable Python functions"
```

---

## Day 6 — Lambda and Exceptions

Concepts:

* Lambda
* `map`
* `filter`
* `reduce`
* Exception handling
* Custom exceptions

Commit:

```bash
git commit -m "feat: practice functional programming and exceptions"
```

---

## Day 7 — Modules and Packages

Concepts:

* Modules
* Imports
* Packages
* `__init__.py`
* Reusable utilities

Commit:

```bash
git commit -m "feat: add Python modules and packages"
```

---

## Day 8 — Decorators

Concepts:

* Higher-order functions
* Closures
* Decorators
* `functools.wraps`
* Practical decorators

Commit:

```bash
git commit -m "feat: implement Python decorators"
```

---

## Day 9 — Iterators and Generators

Concepts:

* Iterables
* Iterators
* `iter`
* `next`
* `StopIteration`
* `yield`
* Generator expressions
* Lazy evaluation

Commit:

```bash
git commit -m "feat: implement iterators and generators"
```

---

## Day 10 — Context Managers and Python Execution

Concepts:

* Context managers
* `with`
* `__enter__`
* `__exit__`
* `contextlib`
* Python execution model
* `__name__`
* `__main__`
* Bytecode basics

Commit:

```bash
git commit -m "feat: practice context managers and Python execution"
```

---

# Exercises

Every major section contains practical exercises.

Exercises progress through:

```text
Easy
  ↓
Medium
  ↓
Hard
  ↓
ML/AI-Oriented
```

Examples include:

* Building feature processors
* Validating model configurations
* Processing datasets
* Creating reusable utilities
* Building configuration loaders
* Implementing lazy data pipelines
* Creating decorators for logging and timing
* Building generators for batch processing

Solutions are maintained separately so that the exercises can first be attempted independently.

---

# Testing

Tests use `pytest`.

Run all tests with:

```bash
pytest
```

Tests should cover:

* Normal cases
* Edge cases
* Invalid input
* Exceptions
* Reusable functions
* Utility modules
* Generators
* Iterators
* Context managers

Example:

```python
def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20
```

---

# Final Project — ML Data Pipeline

The chapter concludes with an ML-oriented Python project.

```text
projects/
└── ml_data_pipeline/
    ├── README.md
    ├── requirements.txt
    │
    ├── data/
    │   └── sample_data.csv
    │
    ├── src/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── loader.py
    │   ├── validator.py
    │   ├── processor.py
    │   └── pipeline.py
    │
    └── tests/
        ├── test_loader.py
        ├── test_validator.py
        └── test_processor.py
```

The pipeline will demonstrate:

```text
CSV Dataset
    ↓
Loader
    ↓
Validation
    ↓
Cleaning
    ↓
Processing
    ↓
Feature Preparation
    ↓
Output Dataset
```

The project will use Python fundamentals such as:

* Variables
* Data structures
* Functions
* Exceptions
* Modules
* Packages
* Decorators
* Generators
* Context managers
* Testing

---

# ML/AI Connection

Python fundamentals will be connected to future AI/ML engineering work.

For example:

### Configuration

```python
model_config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 10,
}
```

### Feature data

```python
features = [0.2, 0.5, 0.8, 0.9]
```

### Batch generation

```python
def generate_batches(data, batch_size):
    for start in range(0, len(data), batch_size):
        yield data[start:start + batch_size]
```

### Validation

```python
if not features:
    raise ValueError("features cannot be empty")
```

These concepts will later appear inside:

* Data pipelines
* ML training loops
* FastAPI services
* RAG pipelines
* LLM applications
* AI agents
* Production AI systems

---

# How to Run

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run an example:

```bash
python 01_variables_and_types/variables.py
```

Run tests:

```bash
pytest
```

---

# Git Workflow

Each learning session should result in a meaningful commit.

Typical workflow:

```bash
git status
git add .
git commit -m "feat: implement Python functions"
git push origin main
```

The commit history should demonstrate the progression of the learning process.

---

# Interview Preparation

By the end of this chapter, I should be able to answer questions such as:

1. What is the difference between a list and tuple?
2. What is mutable vs immutable in Python?
3. How does Python manage variables?
4. What are `*args` and `**kwargs`?
5. What is the difference between `is` and `==`?
6. What is a decorator?
7. What is a generator?
8. What is the difference between an iterable and iterator?
9. Why are generators memory efficient?
10. What is a context manager?
11. What does `with` do?
12. What is `__name__ == "__main__"`?
13. How does Python execute source code?
14. What is the difference between a module and package?
15. How should exceptions be handled in production Python code?

---

# Progress Checklist

## Variables and Types

* [ ] Variables
* [ ] Data types
* [ ] Type conversion
* [ ] Mutability
* [ ] Immutability

## Strings

* [ ] String operations
* [ ] String methods
* [ ] Formatting
* [ ] f-strings
* [ ] Text normalization

## Data Structures

* [ ] Lists
* [ ] Tuples
* [ ] Sets
* [ ] Dictionaries

## Control Flow

* [ ] Conditions
* [ ] `for`
* [ ] `while`
* [ ] `break`
* [ ] `continue`

## Comprehensions

* [ ] List comprehensions
* [ ] Dictionary comprehensions
* [ ] Set comprehensions

## Functions

* [ ] Functions
* [ ] Parameters
* [ ] Return values
* [ ] Type hints
* [ ] Scope
* [ ] `*args`
* [ ] `**kwargs`

## Functional Programming

* [ ] Lambda
* [ ] `map`
* [ ] `filter`
* [ ] `reduce`

## Exceptions

* [ ] `try`
* [ ] `except`
* [ ] `else`
* [ ] `finally`
* [ ] Custom exceptions

## Modules and Packages

* [ ] Modules
* [ ] Imports
* [ ] Packages
* [ ] `__init__.py`
* [ ] `__main__`

## Decorators

* [ ] Higher-order functions
* [ ] Closures
* [ ] Decorators
* [ ] `functools.wraps`

## Iterators

* [ ] Iterable
* [ ] Iterator
* [ ] `iter`
* [ ] `next`
* [ ] `StopIteration`

## Generators

* [ ] `yield`
* [ ] Generator functions
* [ ] Generator expressions
* [ ] Lazy evaluation

## Context Managers

* [ ] `with`
* [ ] `__enter__`
* [ ] `__exit__`
* [ ] `contextlib`
* [ ] Custom context managers

## Python Execution

* [ ] Source code
* [ ] Parsing
* [ ] Bytecode
* [ ] Python Virtual Machine
* [ ] Namespaces
* [ ] Imports
* [ ] `__name__`
* [ ] `__main__`

## Final Project

* [ ] ML data pipeline
* [ ] Data loading
* [ ] Validation
* [ ] Processing
* [ ] Error handling
* [ ] Tests
* [ ] Documentation

---

# Completion Criteria

Chapter 1 is complete when I can:

```text
Write Python
     ↓
Explain Python
     ↓
Structure Python
     ↓
Test Python
     ↓
Debug Python
     ↓
Build reusable Python components
     ↓
Apply Python to ML/AI problems
```

The final objective is not simply to memorize Python syntax.

The objective is to become comfortable enough with Python that the language itself does not become a bottleneck when moving into:

**NumPy → Pandas → Machine Learning → PyTorch → Deep Learning → NLP → Transformers → LLMs → Fine-Tuning → RAG → Agents → Production AI**

---

## Status

**Chapter:** 1 — Python Fundamentals

**Status:** 🟡 In Progress

**Next:** Day 1 — Variables, Data Types & Strings

#variable assignment
user_name = "ravindra"
items_in_cart = 5

#dynamic typing
#variables 'status' can be changed to any value of any type
status = 200
# status = "success"

#type inspection
# use type() to inspect the what calss obejct belongs to at runtime
print(type(status))
print(type(items_in_cart))

#output we get for the above type checking
# <class 'int'>
# <class 'int'>

#advanced variable assignment

import os
from typing import  Optional, Union, Callable, Any

#variable scope , the global scope and local scope 
# By default, assigning a variable inside a function creates a local variable.
# To modify variables in outer scopes, we use specific keywords.


system_status = "stable"

def outer_function():
    count = 0

    def inner_function():
        nonlocal count
        global system_status

        count += 1

        system_status = "Running"
    inner_function()
    return count
    # print(f"Count inside outer_function: {count}")

#advanced type hinting (PEP 484 & PEP 604)
# PEP means Python Enhancement Proposal.

#type hinting is a way to indicate the expected data types of variables, function parameters, and return values in Python. It helps improve code readability and can assist with static type checking.

user_id: int | str = 404

#optional types

user_mail: Optional[str] = None

#callable -> variabel is a function that makes specific arguments and returns a specific type
# for suppose takes an int and returns the boolean value

validator_func : Callable[[int], bool] = lambda x: x < 0

#Any explicity opt out of the type checking for this varaible

dynamic_data: Any = {"key": "value"}

# Dunder variables (Double Underscore Variables)
# Dunder variables are special variables in Python that have double underscores at the beginning and end of
# their names. They are also known as "magic" or "special" variables. Dunder variables are used to define special methods and attributes that have specific meanings in Python.

if __name__ == "__main__":
    outer_function()
    print(f"System status: {system_status}")

#__file__ contains the path to the current script file
# print(f"Script file: {__file__}")

#__dict__ stores the namespace of the current module, class, or object as a dictionary. It allows you to access and manipulate the attributes and methods of the object dynamically.
class config:
    timeout = 30

print(f"Config timeout: {config.__dict__['timeout']}"
)
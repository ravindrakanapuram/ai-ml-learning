# --- Creating Lists ---
fruits = ["apple", "banana", "cherry"]
mixed = [1, "two", 3.0, True]

# --- Indexing & Slicing ---
first = fruits[0]            # 'apple'
last = fruits[-1]            # 'cherry'
sub_list = fruits[0:2]       # ['apple', 'banana']

# --- Adding Elements ---
fruits.append("date")        # Adds to the end
fruits.insert(1, "mango")    # Inserts at a specific index
fruits.extend(["fig", "grape"]) # Merges another sequence into the list

# --- Removing Elements ---
fruits.remove("banana")      # Removes the first matching value
popped_item = fruits.pop()   # Removes and returns the last item (or item at given index)
# fruits.clear()             # Empties the entire list

# --- Sorting ---
numbers = [4, 1, 7, 3]
numbers.sort()               # Sorts in-place: [1, 3, 4, 7]
numbers.sort(reverse=True)   # Sorts descending
sorted_nums = sorted([9, 2]) # Returns a new sorted list: [2, 9]

# --- Iteration ---
for fruit in fruits:
    print(fruit.upper())
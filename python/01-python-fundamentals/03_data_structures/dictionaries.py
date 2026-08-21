# --- Key/Value Pairs ---
user = {
    "username": "ada_lovelace",
    "role": "admin",
    "active": True
}

# --- Lookup ---
name = user["username"]       # 'ada_lovelace' (Raises KeyError if missing)
status = user.get("active")   # True
age = user.get("age", 25)     # 25 (Returns default value if key is missing)

# --- Updating Values ---
user["role"] = "superadmin"   # Updates existing key
user["last_login"] = "today"  # Adds a new key/value pair

user.update({"active": False, "theme": "dark"}) # Updates/adds multiple pairs

# --- Iteration ---
# Iterating over keys (default behavior)
for key in user:
    print(key)

# Iterating over values
for value in user.values():
    print(value)

# Iterating over key-value pairs
for key, value in user.items():
    print(f"{key}: {value}")

# --- Nested Dictionaries ---
company = {
    "engineering": {
        "manager": "Alice",
        "employees": 15
    },
    "sales": {
        "manager": "Bob",
        "employees": 5
    }
}

eng_manager = company["engineering"]["manager"] # 'Alice'
# --- Immutable Sequences ---
coordinates = (40.7128, -74.0060)
single_item_tuple = ("lonely",)  # Comma is required for a single-item tuple
# coordinates[0] = 41.0          # TypeError: 'tuple' object does not support item assignment

# --- Tuple Unpacking ---
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# --- Returning Multiple Values ---
def get_user_info():
    # Functions naturally pack multiple comma-separated return values into a tuple
    return "Ada", 30, "admin" 

name, age, role = get_user_info() # Unpacking the returned tuple directly
# --- Unique Values ---
# Duplicates are automatically removed
colors = {"red", "blue", "red", "green"} # Evaluates to {'blue', 'green', 'red'}
empty_set = set() # {} creates an empty dictionary, not a set

# --- Mathematical Set Operations ---
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Elements in either set
union_set = set_a | set_b               # {1, 2, 3, 4, 5, 6}

# Intersection: Elements in both sets
intersect_set = set_a & set_b           # {3, 4}

# Difference: Elements in A but not in B
diff_set = set_a - set_b                # {1, 2}
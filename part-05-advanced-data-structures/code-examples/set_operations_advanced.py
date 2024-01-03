# set_operations_advanced.py

# Creating sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2, 3}

# Checking for subset
is_subset = set_c.issubset(set_a)
print(f"Set C is a subset of Set A: {is_subset}")

# Checking for superset
is_superset = set_a.issuperset(set_c)
print(f"Set A is a superset of Set C: {is_superset}")

# Checking for disjoint sets (no common elements)
set_d = {6, 7, 8, 9}
is_disjoint = set_a.isdisjoint(set_d)
print(f"Set A and Set D are disjoint: {is_disjoint}")

# Intersection of sets
intersection = set_a.intersection(set_b)
print(f"Intersection of Set A and Set B: {intersection}")

# Union of sets
union = set_a.union(set_b)
print(f"Union of Set A and Set B: {union}")

# Difference of sets
difference = set_a.difference(set_b)
print(f"Difference of Set A and Set B: {difference}")

# Symmetric difference of sets (elements in either set, but not in both)
symmetric_difference = set_a.symmetric_difference(set_b)
print(f"Symmetric difference of Set A and Set B: {symmetric_difference}")

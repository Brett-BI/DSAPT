# Sets
In Python, sets are implemented as hash tables. Think of them like a dictionary with keys and no values. Under the hood, sets rely on hashes for insertions and lookups. 

Sidenote: implementing sets, in Python, means that a `__eq__()` needs to be created for comparison and `__hash__()` to generate the hash.

# Features
Many of the same features as dictionaries: 
- Look-ups in O(1) time
- Inserts in O(1)
- Delete in O(1)
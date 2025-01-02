# Hash Tables
## Overview
Generally speaking, a hash table is a data structure comprised of indexed set of key:value pairs. Each key in the hash table corresponds to a value. This is, essentially, a dictionary in Python (Python actually implements a specific hashing function to create a dictionary).

Lookups are O(1) because we have a key for the item.

## Under the Hood
A hashing function is used on the key to convert it into a fixed-size integer (known as the *hash code* or *hash value*). Under the hood, this is referenced in memory? This hash value becomes the index for the array of values.

Collisions are an issue in hashtables. Because each index needs to be unique, attempting to add an item with the same index causes a collision. Collisions must be handled by either:
1. Chaining: storing multiple values at the same index using a linked list or similar data structure
2. Open Addressing: adding the item to the next available slot in the array

## Issues & Limitations
Duplicates cause errors: one key cannot point to multiple values.
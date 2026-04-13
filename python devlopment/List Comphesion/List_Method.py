# Initial list
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# 1. Counting occurrences
print(f"Apples: {fruits.count('apple')}")        # Output: 2
print(f"Tangerines: {fruits.count('tangerine')}") # Output: 0

# 2. Finding indices
print(f"First banana index: {fruits.index('banana')}")    # Output: 3
print(f"Next banana after index 4: {fruits.index('banana', 4)}") # Output: 6

# 3. Reversing the list
fruits.reverse()
print(f"Reversed: {fruits}")

# 4. Appending a single item
fruits.append('grape')
print(f"After append: {fruits}")

# 5. Sorting alphabetically
fruits.sort()
print(f"Sorted: {fruits}")

# 6. Popping (removes and returns the last item)
last_item = fruits.pop()
print(f"Popped item: {last_item}")

# --- NEW METHODS ---

# 7. Extend: Adding multiple items at once
more_fruits = ['mango', 'strawberry']
fruits.extend(more_fruits)
print(f"After extend: {fruits}")

# 8. Insert: Adding 'blueberry' at the second position (index 1)
fruits.insert(1, 'blueberry')
print(f"After insert: {fruits}")

# 9. Remove: Deleting the first 'apple' found
fruits.remove('apple')
print(f"After remove: {fruits}")

# 10. Clear: Emptying the list entirely
fruits.clear()
print(f"Final cleared list: {fruits}")
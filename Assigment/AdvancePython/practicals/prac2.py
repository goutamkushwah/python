# WAP for implementing all the operation of string in python.

# String declaration
s1 = "JEC i a well recognized institute."
s2 = "I am a student of JEC."

print("s1 =", s1)
print("s2 =", s2)

# Length of string
print("Length of s1:", len(s1))

# String concatenation
concat = s1 + " " + s2
print("Concatenation:", concat)

# String repetition
repeat = s2 * 2
print("Repetition:", repeat)

# String indexing and slicing
print("First character of s1:", s1[0])
print("Last character of s1:", s1[-1])
print("Substring (0 to 5):", s1[0:5])
print("Substring (6 to end):", s1[6:])

# String membership
print("'JEC' in s1:", "JEC" in s1)
print("'JEC' not in s2:", "JEC" not in s2)

# Case conversion
print("Uppercase:", s1.upper())
print("Lowercase:", s2.lower())
print("Title case:", s2.title())
print("Swap case:", s1.swapcase())

# Searching strings
print("Index of 'well':", s1.find("well"))
print("Count of 'o' in s1:", s1.count("o"))

# String replacement
replaced = s1.replace("JEC", "MTSS")
print("After replacement:", replaced)

# # Removing whitespace
# s3 = "   Hello Python   "
# print("Original:", s3)
# print("After strip():", s3.strip())
# print("After lstrip():", s3.lstrip())
# print("After rstrip():", s3.rstrip())

# Splitting and joining
words = s2.split()
print("Split string:", words)

joined = "-".join(words)
print("Joined string:", joined)

# String comparison
print("s1 == s2:", s1 == s2)
print("s1 < s2:", s1 < s2)


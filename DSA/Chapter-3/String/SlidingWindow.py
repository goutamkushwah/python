s = "aeioubcdf"
k = 3
vowels = "aeiou"

count = 0
for ch in s[:k]:
    if ch in vowels:
        count += 1

max_count = count

for i in range(k, len(s)):
    if s[i] in vowels:
        count += 1
    if s[i-k] in vowels:
        count -= 1
    max_count = max(max_count, count)

print(max_count)

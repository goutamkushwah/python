<<<<<<< HEAD
# Date - 24/11/2025
# Python program to count vowels, consonants and blank spaces in a string

s = "my name is goutam kushwah"
vowels = 0
consonants = 0
blanks = 0

vol = ["a","e","i","o","u","A","E","I","O","U"]
bla = [" "]
for ch in s:
    if ch in vol:
        vowels += 1
    elif ch in bla:
        blanks += 1
    else:
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Blank spaces =", blanks)
=======
# Date - 24/11/2025
# Python program to count vowels, consonants and blank spaces in a string

s = "my name is goutam kushwah"
vowels = 0
consonants = 0
blanks = 0

vol = ["a","e","i","o","u","A","E","I","O","U"]
bla = [" "]
for ch in s:
    if ch in vol:
        vowels += 1
    elif ch in bla:
        blanks += 1
    else:
        consonants += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Blank spaces =", blanks)
>>>>>>> 26cc84673f9c4c64d6378a4e42a701fed508568a

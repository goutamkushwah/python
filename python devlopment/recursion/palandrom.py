# def is_palindrome(word):
#      """Return True if word is a palindrome, False if not."""
#      if len(word) <= 1:
#          return True
#      else:
#           return word[0] == word[-1] and is_palindrome(word[1:-1])
# print(is_palindrome("abcba"))
# print(is_palindrome("abcda"))


def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
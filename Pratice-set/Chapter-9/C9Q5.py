# Date 06-10-2025
# Repeat program 4 for a list of such words to be censored. 
words = ["Donkey", "bad", "ganda"]

with open("Pratice-set/Chapter-9/file.txt", "r") as f:
    content = f.read()
for word in words:
  contentNew = content.replace(word, "######")

with open("Pratice-set/Chapter-9/file.txt", "w") as f:
    f.write(contentNew)
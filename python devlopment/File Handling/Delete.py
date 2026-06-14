import os
if os.path.exists("b.txt"):
  os.remove("b.txt")
else:
  print("The file does not exist")
str_counter = 0

for item in ("Alice", 30, "Programmer", None, True, "Department C"):
     if isinstance(item, str):
          str_counter += 1


print(str_counter)

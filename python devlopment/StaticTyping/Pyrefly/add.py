def add(a: int, b: int):   # ✅ param annotations
  return a + b    # 🔍 return inferred -> int
print(add(1,2) )
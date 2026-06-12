import pandas as pd

data = {
    "Name": ["Goutam", "Rahul", "Aman"],
    "Age": [22, 23, 21],
    "City": ["Indore", "Mumbai", "Delhi"]
}

df = pd.DataFrame(data)
print(df)
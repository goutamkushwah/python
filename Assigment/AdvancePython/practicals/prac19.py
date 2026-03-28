# WAP for Pandas in python

# -------------------------------------
# WAP FOR PANDAS IN PYTHON
# -------------------------------------

import pandas as pd

# 1️⃣ Creating a Series
data_series = pd.Series([10, 20, 30, 40])
print("Series:")
print(data_series)
print()


# 2️⃣ Creating a DataFrame
data = {
    "Name": ["Manish", "Rahul", "Amit"],
    "Age": [21, 22, 23],
    "Course": ["BCA", "BSc", "BCom"]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)
print()


# 3️⃣ Display Basic Information
print("Shape of DataFrame:", df.shape)
print("Columns:", df.columns)
print()


# 5️⃣ Filtering Data
print("Students Age > 21:")
print(df[df["Age"] > 21])
print()


# 6️⃣ Adding New Column
df["Marks"] = [85, 90, 88]
print("After Adding Marks Column:")
print(df)
print()


# 7️⃣ Deleting Column
df.drop("Course", axis=1, inplace=True)
print("After Deleting Course Column:")
print(df)
print()


# 8️⃣ Statistical Functions
print("Average Age:", df["Age"].mean())
print("Maximum Marks:", df["Marks"].max())
print()


# 9️⃣ Saving to CSV
df.to_csv("students.csv", index=False)
print("Data saved to students.csv")
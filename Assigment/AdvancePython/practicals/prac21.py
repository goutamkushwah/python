# WAP for Seaborn Statistical Plots in AP.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Math_Marks": [78, 85, 96, 65, 70, 88, 92, 75, 84, 90],
    "Science_Marks": [72, 80, 94, 60, 68, 85, 89, 70, 82, 88],
    "Class": ["X", "Z", "X", "Y", "Z", "Y", "X", "Z", "X", "Y"]
})

# Create figure
plt.figure(figsize=(10, 5))

# --------------------------------
# 1. Histogram
# --------------------------------
plt.subplot(2, 2, 1)
sns.histplot(data["Math_Marks"], kde=True)
plt.title("Histogram")

# --------------------------------
# 2. Box Plot
# --------------------------------
plt.subplot(2, 2, 2)
sns.boxplot(x="Class", y="Math_Marks", data=data)
plt.title("Box Plot by Class")

plt.subplot(2, 2, 4)
sns.regplot(x="Math_Marks", y="Science_Marks", data=data)
plt.title("Math vs Science (Regression)")



# Adjust layout
plt.tight_layout()

# Show all plots
plt.show()
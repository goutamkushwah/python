import matplotlib.pyplot as plt

# -----------------------------
# Data for Line Chart
# -----------------------------
x = [1, 2, 3, 4, 5]
sales_2023 = [100, 200, 250, 300, 400]
sales_2024 = [150, 220, 270, 350, 450]

# -----------------------------
# Data for Bar Chart
# -----------------------------
products = ["Product A", "Product B", "Product C", "Product D"]
revenue = [50, 80, 60, 90]

# -----------------------------
# Data for Pie Chart
# -----------------------------
departments = ["HR", "IT", "Finance", "Marketing"]
budget = [20, 40, 25, 15]

# -----------------------------
# Create Subplots (1 row, 3 columns)
# -----------------------------
plt.figure(figsize=(15, 5))

# --------- Multi Line Chart ----------
plt.subplot(1, 3, 1)
plt.plot(x, sales_2023, marker='o', label="Sales 2023")
plt.plot(x, sales_2024, marker='o', label="Sales 2024")
plt.title("Multi-Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

# --------- Bar Chart ----------
plt.subplot(1, 3, 2)
plt.bar(products, revenue)
plt.title("Bar Chart")
plt.xlabel("Products")
plt.ylabel("Revenue")

# --------- Pie Chart ----------
plt.subplot(1, 3, 3)
plt.pie(budget, labels=departments, autopct='%1.1f%%')
plt.title("Pie Chart")

# Adjust layout
plt.tight_layout()

# Display all charts
plt.show()
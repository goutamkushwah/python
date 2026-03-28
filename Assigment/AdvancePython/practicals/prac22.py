#WAP for Scikit-Learn(Machine Learning) in AP.
# # Import Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ------------------------------------
# Step 1: Create Own Dataset
# ------------------------------------
data = pd.DataFrame({
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks_Scored": [35, 40, 50, 55, 65, 70, 75, 85, 90, 95]
})

# ------------------------------------
# Step 2: Define Features and Target
# ------------------------------------
X = data[["Hours_Studied"]]   # Independent Variable
y = data["Marks_Scored"]      # Dependent Variable

# ------------------------------------
# Step 3: Split Dataset
# ------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------------
# Step 4: Create Model
# ------------------------------------
model = LinearRegression()

# ------------------------------------
# Step 5: Train Model
# ------------------------------------
model.fit(X_train, y_train)

# ------------------------------------
# Step 6: Make Predictions
# ------------------------------------
y_pred = model.predict(X_test)

# ------------------------------------
# Step 7: Evaluate Model
# ------------------------------------
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Predicted Marks:", y_pred)
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# ------------------------------------
# Step 8: Predict for New Data
# ------------------------------------
new_hours = np.array([[12]])
predicted_marks = model.predict(new_hours)
print("Predicted Marks for 12 hours study:", predicted_marks)
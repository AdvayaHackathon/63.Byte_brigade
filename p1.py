


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# 1. Load the dataset
# Replace with your actual dataset filename
df = pd.read_csv("C:/Users/abhij/OneDrive/Desktop/heart_disease_inputs_dataset.csv")

# 2. Check the columns
print("Columns in dataset:", df.columns)

# 3. Separate features and target
# Replace 'target' with the actual name of your label column
X = df.drop("Smoking", axis=1)
y = df["Family_History"]
print(type(y))
print(y.head())
print(y.shape)

# 4. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate accuracy (optional)
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

# 7. Save the retrained model
with open("heartdiseaseprediction1", "wb") as f:
    pickle.dump(model, f)

print("Model retrained and saved as 'heartdiseaseprediction1'")



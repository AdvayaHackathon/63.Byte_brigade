import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle


data = pd.read_csv("heart_disease_inputs_dataset.csv")
print(data.head())

print(data.isnull().sum())

features = data[["Age", "Weight", "Height", "Smoking", "Alcohol", "Exercise Frequency", "Diet Type", "Sleep Timings","Symptoms","Family History"]]
target = data['Heart Disease']

print(features)
print(target)

x_train, x_test, y_train, y_test = train_test_split(features, target, random_state = 3136)

model = RandomForestClassifier()
model.fit(x_train, y_train)

"""
print(model.feature_importances_)
x = features.columns
y = model.feature_importances_
plt.bar(x,y)
plt.xlabel("Features")
plt.ylabel("Importances")
plt.show()


#important features --> Age, Chest Pain, BP, cholestrol, Max_HR(max heart rate), ST_depression, Number of vessels fluro, Thallium
# what to drop --> sex, FBS over 12kg, EKG results, excercise angina, slope of ST

"""

y_pred = model.predict(x_test)

print(x_test)
print(y_test)
print(y_pred)

cr = classification_report(y_pred, y_test)
print(cr)


with open("heartdiseaseprediction.model", "wb") as f:
	pickle.dump(model, f)


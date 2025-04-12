# heart-disease-prediction
Introduction-
This is a fully validated multi-user application, where a user can check if he/she has heart disease or not by filling a short form which collects data from the heart disease prediction model and returns with a response based on the dataset used. 

Keywords- 
ML, Flask, RandomForestClassifier, HTML, CSS, Bootstrap

Dataset-
Heart Disease Prediction dataset from kaggle.com
Link - https://www.kaggle.com/rishidamarla/heart-disease-prediction

Machine Learning - 
Made use of Random Forest Classifier Algorithm, used random state = 3136

Model prediction Accuracy - 
70%

Flask-
Backend of the entire web application has been programmed in Flask, with a app.py controlling the major functionalities and the connections to all pages. 
Used Flask mail for sending randomly generated passwords to users when they try to sign in, and will then be redirected to the login page as soon as we send the email containing the password of the particular user. 
Re-using the same username won't be possible as it has been set as the primary key. 
A forgot password page has been made just in case the user forgets their password to the application.
All the forms are fully validated, including the quiz form inside which is the main functionality of the application. Responses to the form are used alongside the data present in the dataset to make the prediction.

HTML, CSS, BOOTSTRAP -
The entire frontend of the application have been made using html, css and bootstrap. And the application is fully responsive and is fully functional on all device widths.

Database-Sqlite3
name - monicaheart.db
table name - user

PROJECT DONE BY:
TEAM NAME: BYTE BRIGADE
TEAM MEMBERS:
SINCHANA KUTTAPPA K
ABHIJNA N P
ANKITHA VENKAT
PRANIDHI K K








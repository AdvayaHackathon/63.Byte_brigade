from flask import Flask, render_template, request, redirect, session, url_for
from sqlite3 import *
import pickle

app = Flask(__name__)
app.secret_key = "monicaheart"

@app.route("/")
def home():
    if 'username' in session:
        return render_template("home.html", name = session['username'])
    else:
        return redirect(url_for('signup'))

@app.route("/find")
def find():
    if 'username' in session:
        return render_template("find.html", name = session['username'])
    else:
        return redirect(url_for('home'))

@app.route("/check", methods = ["POST"])
def check():
    if request.method == "POST":
        if 'username' in session:
            name = session['username']
        age = float(request.form["age"])
        '''r1 = request.form["r1"]
        if r1 == "1":
            cp = 1
        elif r1 == "2":
            cp = 2    
        elif r1 == "3":
            cp = 3
        else:
            cp = 4'''
       # Age = float(request.form["Age"])
        Weight = float(request.form["Weight"])
        Height = float(request.form["Height"])
        Sex = float(request.form["Sex"])
        Smoking = float(request.form["Smoking"])
        Alcohol = float(request.form["Alcohol"])
        Exercise_Frequency = float(request.form["Exercise_Frequency"])
        Diet_Type = float(request.form["Diet_Type"])
        Sleep_Timings = float(request.form["Sleep_Timings"])
        Symptoms = float(request.form["Symptoms"])
        Family_History = float(request.form["Family_History"])

        d = [[age, Weight, Height, Sex, Smoking, Alcohol, Exercise_Frequency, Diet_Type,Sleep_Timings,Symptoms,Family_History]]    
        with open("heartdiseaseprediction.model", "rb") as f:
            model = pickle.load(f)    
        res = model.predict(d)
        return render_template("find.html", msg = res, name = session['username'])    
    else:
        return render_template("home.html")

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        #em = request.form["em"]
        un = request.form["un"]
        pw = request.form["pw"]  # Get password directly from form
        
        con = None
        try:
            con = connect("monicaheart.db")
            cursor = con.cursor()
            sql = "insert into user values('%s', '%s')"  # Modified to include
            cursor.execute(sql % (un, pw))  # Store username, password
            con.commit()
            return render_template("login.html", msg = "Account created successfully. Please login.")
        except Exception as e:
            con.rollback()
            return render_template("signup.html", msg = "User already exists: " + str(e))
    else:
        return render_template("signup.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        un = request.form["un"]
        pw = request.form["pw"]
        con = None
        try:
            con = connect("monicaheart.db")
            cursor = con.cursor()
            sql = "select * from user where username = '%s' and password = '%s'"
            cursor.execute(sql % (un, pw))
            data = cursor.fetchall()
            if len(data) == 0:
                return render_template("login.html", msg = "Invalid username or password")
            else:    
                session['username'] = un
                return redirect(url_for('home'))
        
        except Exception as e:
            msg = "Issue " + str(e)
            return render_template("login.html", msg = msg)
    else:
        return render_template("login.html")

@app.route("/forgot", methods = ["GET", "POST"])
def forgot():
    if request.method == "POST":
        un = request.form["un"]
       # em = request.form["em"]
        con = None
        try:
            con = connect('monicaheart.db')        
            cursor = con.cursor()
            sql = "select * from user where username = '%s' and email = '%s'"
            cursor.execute(sql % (un))
            data = cursor.fetchall()
            if len(data) == 0:
                return render_template("forgot.html", msg = "Username or email not found")
            else:    
                session['reset_user'] = un
                return redirect(url_for('reset_password'))
        except Exception as e:
            msg = "Issue " + str(e)
            return render_template("forgot.html", msg = msg)    
    else:
        return render_template("forgot.html")

@app.route("/reset_password", methods = ["GET", "POST"])
def reset_password():
    if 'reset_user' not in session:
        return redirect(url_for('forgot'))
        
    if request.method == "POST":
        new_pw = request.form["new_pw"]
        confirm_pw = request.form["confirm_pw"]
        
        if new_pw != confirm_pw:
            return render_template("reset_password.html", msg = "Passwords don't match")
            
        un = session['reset_user']
        con = None
        try:
            con = connect("monicaheart.db")
            cursor = con.cursor()
            sql = "update user set password = '%s' where username = '%s'"
            cursor.execute(sql % (new_pw, un))
            con.commit()
            session.pop('reset_user', None)
            return render_template("login.html", msg = "Password has been reset successfully")
        except Exception as e:
            con.rollback()
            return render_template("reset_password.html", msg = "Error: " + str(e))
    else:
        return render_template("reset_password.html")

@app.route("/logout", methods = ["POST"])
def logout():
    session.clear()    
    return redirect(url_for("login"))

@app.route("/setup_db")
def setup_db():
    con = connect("monicaheart.db")
    cursor = con.cursor()
    # Drop the existing table if it exists
    cursor.execute("DROP TABLE IF EXISTS user")
    # Create the new table with email field
    cursor.execute("CREATE TABLE user (username TEXT PRIMARY KEY, password TEXT, email TEXT)")
    con.commit()
    con.close()
    return "Database setup complete"

if __name__ == "__main__":
    app.run(debug = True)

'''from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/checking', methods=['POST'])
def checking():
    # Collecting Form Data
    age = request.form['age']
    weight = request.form['weight']
    height = request.form['height']
    sex = request.form['sex']
    smoking = request.form['smoking']
    alcohol = request.form['alcohol']
    exercise = request.form['exercise']
    diet = request.form['diet']
    sleep = request.form['sleep']
    symptoms = request.form.getlist('symptoms')  # For multiple checkboxes
    family = request.form['family']

    # Just for testing - Printing data in console
    print("Age:", age)
    print("Weight:", weight)
    print("Height:", height)
    print("Sex:", sex)
    print("Smoking:", smoking)
    print("Alcohol:", alcohol)
    print("Exercise:", exercise)
    print("Diet:", diet)
    print("Sleep:", sleep)
    print("Symptoms:", symptoms)
    print("Family History:", family)

    # Here you can add your ML model prediction logic
    # Example:
    # result = model.predict([[age, weight, height, ...]])

    # For now, simple condition for demo:
    if "Chest Pain" in symptoms or "Shortness of Breath" in symptoms or family == "Yes":
        msg = "High Risk of Heart Disease"
    else:
        msg = "Low Risk of Heart Disease"

    return render_template('index.html', msg=msg)


if __name__ == '__main__':
  app.run(debug=True)'''


'''from flask import Flask, render_template, request, redirect, session, url_for
from sqlite3 import *
import pickle

app = Flask(__name__)
app.secret_key = "monicaheart"

@app.route("/")
def home():
    if 'username' in session:
        return render_template("home.html", name=session['username'])
    else:
        return redirect(url_for('signup'))

@app.route("/find")
def find():
    if 'username' in session:
        return render_template("find.html", name=session['username'])
    else:
        return redirect(url_for('home'))

@app.route("/check", methods=["POST"])
def check():
    if request.method == "POST":
        if 'username' in session:
            name = session['username']

        age = float(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        sex = 1 if request.form["sex"] == "male" else 0
        smoking = float(request.form["smoking"])
        alcohol = float(request.form["alcohol"])
        exercise = float(request.form["exercise"])
        diet = float(request.form["diet"])
        sleep = float(request.form["sleep"])
        symptoms = float(request.form["symptoms"])
        family = float(request.form["family"])

        d = [[age, weight, height, sex, smoking, alcohol, exercise, diet, sleep, symptoms, family]]

        with open("heartdiseaseprediction.model", "rb") as f:
            model = pickle.load(f)

        res = model.predict(d)
        return render_template("find.html", msg=res, name=session['username'])
    else:
        return render_template("home.html")

# other routes remain unchanged

if __name__ == "__main__":
    app.run(debug=True)'''

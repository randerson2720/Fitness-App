from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import pymysql
pymysql.install_as_MySQLdb()
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import datetime


app = Flask(__name__)

app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "fitness"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
 
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/delete/<int:id>")
def delete_user(id):
    cursor = mysql.connection.cursor()
    delete_query = "DELETE FROM users WHERE UserID = %s"
    try:
        cursor.execute(delete_query, (id))
        mysql.connection.commit()
        return redirect("/users")
    except:
        return "<h2>There was an error deleting the user.</h2>"

@app.route("/user", methods=["GET", "POST"])
def add_user():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        user_first_name = request.form["userFirstName"]
        user_last_name = request.form["userLastName"]
        user_experience_level = request.form["userExperienceLevel"]
        user_goal = request.form["userGoal"]
        #insert form data
        add_query = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s)"
        cursor.execute(add_query, (user_first_name, user_last_name, user_experience_level, user_goal))
        mysql.connection.commit()
        #redirect to users page
        return redirect("/users")
    else:
        return render_template("user.html", user="", action="user")

@app.route("/user/<int:id>", methods=["POST", "GET"])
def update_user(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        user_first_name = request.form["userFirstName"]
        user_last_name = request.form["userLastName"]
        user_experience_level = request.form["userExperienceLevel"]
        user_goal = request.form["userGoal"]
        update_query = "UPDATE users SET UserFirstName=%s, UserLastName=%s, ExperienceLevel=%s, Goals=%s WHERE UserID=%s"
        try:
            cursor.execute(update_query, (user_first_name, user_last_name, user_experience_level, user_goal, id))
            mysql.connection.commit()
            return redirect("/users")
        except:
            return "<h2>There was an error updating the user</h2>"
    else:
        cursor.execute("SELECT * FROM users WHERE UserID = %s", (id))
        user_to_update = cursor.fetchone()
        return render_template("user.html", user=user_to_update, form_action=f"/user/{id}")
    
@app.route("/users")
def users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users;")
    resultset = cursor.fetchall()
    return render_template("users.html", users=resultset)

@app.route("/exercise/delete/<int:id>")
def delete_exercise(id):
    cursor = mysql.connection.cursor()
    delete_query = "DELETE FROM exercises WHERE ExerciseID = %s"
    try:
        cursor.execute(delete_query, (id))
        mysql.connection.commit()
        return redirect("/exercises")
    except:
        return "<h2>There was an error deleting the exercise.</h2>"

@app.route("/exercise/<int:id>", methods=["POST", "GET"])
def update_exercise(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        exercise_name = request.form["exerciseName"]
        exercise_type = request.form["exerciseType"]
        exercise_description = request.form["exerciseDescription"]
        update_query = "UPDATE exercises SET ExerciseName=%s, ExerciseType=%s, Description=%s WHERE ExerciseID=%s"
        try:
            cursor.execute(update_query, (exercise_name, exercise_type, exercise_description, id))
            mysql.connection.commit()
            return redirect("/exercises")
        except:
            return "<h2>There was an error updating the exercise</h2>"
    else:
        cursor.execute("SELECT * FROM exercises WHERE ExerciseID = %s", (id))
        exercise_to_update = cursor.fetchone()
        return render_template("exercise.html", exercise=exercise_to_update, form_action=f"/exercise/{id}")
    

@app.route("/exercise", methods=["GET", "POST"])
def add_exercise():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        exercise_name = request.form["exerciseName"]
        exercise_type = request.form["exerciseType"]
        exercise_description = request.form["exerciseDescription"]
        #insert form data
        add_query = "INSERT INTO exercises VALUES(NULL, %s, %s, %s)"
        cursor.execute(add_query, (exercise_name, exercise_type, exercise_description))
        mysql.connection.commit()
        #redirect to exercises page
        return redirect("/exercises")
    else:
        return render_template("exercise.html", exercise="", action="exercise")

@app.route("/exercises")
def exercises():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM exercises;")
    resultset = cursor.fetchall()
    return render_template("exercises.html", exercises=resultset)

@app.route("/workout/delete/<int:id>")
def delete_workout(id):
    cursor = mysql.connection.cursor()
    delete_query = "DELETE FROM workouts WHERE WorkoutID = %s"
    try:
        cursor.execute(delete_query, (id))
        mysql.connection.commit()
        return redirect("/workouts")
    except:
        return "<h2>There was an error deleting the workout.</h2>"
    
@app.route("/workout/<int:id>", methods=["POST", "GET"])
def update_workout(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        user_id = request.form["userID"]
        workout_name = request.form["workoutName"]
        workout_type = request.form["workoutType"]
        last_update = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_query = "UPDATE workouts SET UserID=%s, WorkoutName=%s, WorkoutType=%s, LastUpdate=%s WHERE WorkoutID=%s"
        try:
            cursor.execute(update_query, (user_id, workout_name, workout_type, last_update, id))
            mysql.connection.commit()
            return redirect("/workouts")
        except:
            return "<h2>There was an error updating the workout</h2>"
    else:
        cursor.execute("SELECT * FROM workouts WHERE WorkoutID = %s", (id))
        workout_to_update = cursor.fetchone()
        return render_template("workout.html", workout=workout_to_update, form_action=f"/workout/{id}")

@app.route("/workout", methods=["GET", "POST"])
def add_workout():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        user_id = request.form["userID"] 
        workout_name = request.form["workoutName"]
        workout_type = request.form["workoutType"]
        date_created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        last_update = date_created
        #insert form data
        add_query = "INSERT INTO workouts VALUES(NULL, %s, %s, %s, %s, %s)"
        cursor.execute(add_query, (user_id, workout_name, workout_type, date_created, last_update))
        mysql.connection.commit()
        #redirect to workouts page
        return redirect("/workouts")
    else:
        return render_template("workout.html", workout="", action="workout")

@app.route("/workouts")
def workouts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT users.UserID, UserFirstName, UserLastName, workouts.WorkoutID, WorkoutName, WorkoutType, DateCreated, LastUpdate FROM users LEFT JOIN workouts ON users.UserID = workouts.UserID;")
    resultset = cursor.fetchall()
    return render_template("workouts.html", workouts=resultset)

@app.route("/workoutdetail/delete/<int:id>")
def delete_workoutdetail(id):
    cursor = mysql.connection.cursor()
    delete_query = "DELETE FROM workoutdetails WHERE WorkoutDetailID = %s"
    try:
        cursor.execute(delete_query, (id))
        mysql.connection.commit()
        return redirect("/workoutdetails")
    except:
        return "<h2>There was an error deleting the workout detail.</h2>"

@app.route("/workoutdetail/<int:id>", methods=["POST", "GET"])
def update_workoutdetail(id):
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        workout_id = request.form["workoutID"]
        exercise_id = request.form["exerciseID"]
        sets = request.form["sets"]
        reps = request.form["reps"]
        weight = request.form["weight"]
        update_query = "UPDATE workoutdetails SET WorkoutID=%s, ExerciseID=%s, Sets=%s, Reps=%s, Weight=%s WHERE WorkoutDetailID=%s"
        try:
            cursor.execute(update_query, (workout_id, exercise_id, sets, reps, weight, id))
            mysql.connection.commit()
            return redirect("/workoutdetails")
        except:
            return "<h2>There was an error updating the workout detail</h2>"
    else:
        cursor.execute("SELECT * FROM workoutdetails WHERE WorkoutDetailID = %s", (id,))
        workoutdetail_to_update = cursor.fetchone()
        return render_template("workoutdetail.html", workoutdetail=workoutdetail_to_update, form_action=f"/workoutdetail/{id}")

@app.route("/workoutdetail", methods=["GET", "POST"])
def add_workoutdetail():
    cursor = mysql.connection.cursor()
    if request.method == "POST":
        workout_id = request.form["workoutID"]
        exercise_id = request.form["exerciseID"]
        sets = request.form["sets"]
        reps = request.form["reps"]
        weight = request.form["weight"]
        add_query = "INSERT INTO workoutdetails (WorkoutID, ExerciseID, Sets, Reps, Weight) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(add_query, (workout_id, exercise_id, sets, reps, weight))
        mysql.connection.commit()
        return redirect("/workoutdetails")
    else:
        return render_template("workoutdetail.html", workoutdetail="", action="/workoutdetail")

@app.route("/workoutdetails")
def workoutdetails():
    cursor = mysql.connection.cursor()
    cursor.execute("""SELECT wd.WorkoutDetailID, wd.WorkoutID, wd.ExerciseID, wd.Sets, wd.Reps, wd.Weight, 
           w.WorkoutName, w.WorkoutType, 
           e.ExerciseName, e.ExerciseType
           FROM workoutdetails wd
           JOIN workouts w ON wd.WorkoutID = w.WorkoutID
           JOIN exercises e ON wd.ExerciseID = e.ExerciseID;""")
    resultset = cursor.fetchall()
    return render_template("workoutdetails.html", workoutdetails=resultset)

if __name__ == "__main__":
    app.run(debug=True)


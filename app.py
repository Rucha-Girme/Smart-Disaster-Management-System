from flask import Flask, render_template, request, redirect, url_for, session
import psycopg2
import joblib
import os
import requests
import folium
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "smart_disaster_secret"

# PostgreSQL Connection
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)
#-------------Wheather API--------------
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather():
    city = "Pune"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url).json()

    return {
        "temperature": response["main"]["temp"],
        "humidity": response["main"]["humidity"],
        "wind": response["wind"]["speed"]
    }

# Load Machine Learning Model
model = joblib.load(os.path.join("models", "disaster_model.pkl"))


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        try:
            fullname = request.form["fullname"]
            email = request.form["email"]
            password = generate_password_hash(request.form["password"])

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO users (fullname, email, password)
                VALUES (%s, %s, %s)
                """,
                (fullname, email, password)
            )

            conn.commit()
            cursor.close()

            return redirect(url_for("login"))

        except Exception as e:
            conn.rollback()
            return f"Registration Error: {e}"

    return render_template("register.html")

#---------------forgot password---------

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        confirm = request.form["confirm"]

        if password != confirm:
            return "Passwords do not match!"

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        if user is None:
            cursor.close()
            return "Email not found!"

        cursor.execute(
            """
            UPDATE users
            SET password=%s
            WHERE email=%s
            """,
            (password, email)
        )

        conn.commit()
        cursor.close()

        return redirect(url_for("login"))

    return render_template("forgot_password.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cursor = conn.cursor()

        cursor.execute("""
            SELECT fullname, password
            FROM users
            WHERE email=%s
        """,
        (email,))

        user = cursor.fetchone()

        cursor.close()

        if user and check_password_hash(user[1], password):
            session["user"] = user[0]
            return redirect(url_for("dashboard"))

        return "Invalid Email or Password!"

    return render_template("login.html")

# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    weather = get_weather()

    cursor = conn.cursor()

    # Recent Predictions
    cursor.execute("""
        SELECT
            temperature,
            humidity,
            rainfall,
            wind,
            result,
            created_at
        FROM predictions
        ORDER BY created_at DESC
        LIMIT 10
    """)
    predictions = cursor.fetchall()

    # Total Predictions
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total_predictions = cursor.fetchone()[0]

    # High Risk
    cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE result='HIGH RISK OF FLOOD / CYCLONE'
    """)
    high_risk = cursor.fetchone()[0]

    # Safe
    cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE result='SAFE CONDITIONS'
    """)
    safe = cursor.fetchone()[0]

    # Moderate
    cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE result='MODERATE DISASTER RISK'
    """)
    moderate = cursor.fetchone()[0]

    # Heatwave
    cursor.execute("""
        SELECT COUNT(*)
        FROM predictions
        WHERE result='HEATWAVE ALERT'
    """)
    heatwave = cursor.fetchone()[0]

    # Users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    cursor.close()

    return render_template(
        "dashboard.html",
        name=session["user"],
        predictions=predictions,
        total_predictions=total_predictions,
        high_risk=high_risk,
        safe=safe,
        moderate=moderate,
        heatwave=heatwave,
        total_users=total_users,
        temperature=weather["temperature"],
        humidity=weather["humidity"],
        wind=weather["wind"]
    )

# ---------------- PREDICTION ----------------

@app.route("/prediction", methods=["GET", "POST"])
def prediction():

    if "user" not in session:
        return redirect(url_for("login"))

    weather = get_weather()   # <-- This is required

    result = None
    color = "secondary"

    if request.method == "POST":

        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        rainfall = float(request.form["rainfall"])
        wind = float(request.form["wind"])

        prediction = model.predict([[temperature, humidity, rainfall, wind]])[0]

        if prediction == "HIGH":
            result = "HIGH RISK OF FLOOD / CYCLONE"
            color = "danger"

        elif prediction == "MODERATE":
            result = "MODERATE DISASTER RISK"
            color = "warning"

        else:
            result = "SAFE CONDITIONS"
            color = "success"

    return render_template(
        "prediction.html",
        weather=weather,      # <-- VERY IMPORTANT
        result=result,
        color=color
    )

# ---------------- EMERGENCY ----------------

@app.route("/emergency")
def emergency():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("emergency.html")


# ---------------- SAFE ZONE MAP ----------------

@app.route("/map")
def map():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("map.html")

# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(debug=True)
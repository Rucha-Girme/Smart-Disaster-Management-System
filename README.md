# 🌍 Smart Disaster Management System

<p align="center">
  <img src="screenshots/banner.png" alt="Smart Disaster Management System Banner" width="100%">
</p>

### 🚨 AI-Powered Disaster Prediction & Emergency Response System

A **Flask-based web application** that predicts disaster risks using **Machine Learning**, provides **live weather information**, displays **safe zones using Google Maps**, and assists users during emergencies.

---

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_App-black?style=for-the-badge&logo=flask)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=for-the-badge&logo=postgresql)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap)
![OpenWeather](https://img.shields.io/badge/OpenWeather-API-yellow?style=for-the-badge)
![Google Maps](https://img.shields.io/badge/Google-Maps-success?style=for-the-badge&logo=googlemaps)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📌 Project Overview

Natural disasters like **Floods**, **Cyclones**, and **Heatwaves** can cause severe damage to life and property.

The **Smart Disaster Management System** helps users monitor weather conditions, predict disaster risk using Machine Learning, locate emergency services through Google Maps, and access emergency information from a single platform.

The project combines **Artificial Intelligence**, **Weather APIs**, **Database Management**, and **Interactive Maps** to build a practical disaster management solution.

---

# 🌟 Project Highlights

- 🤖 Machine Learning Disaster Prediction
- 🌦 Live Weather using OpenWeather API
- 📍 Google Maps Safe Zone Integration
- 🔐 Secure User Authentication
- 📊 Dashboard with Prediction History
- 🗄 PostgreSQL Database
- 📱 Responsive Bootstrap 5 Interface
- 🚨 Emergency Contact Module
- 🔒 Password Hashing using Werkzeug
- 💻 Built using Flask Framework

---

# ✨ Features

### 👤 User Authentication
- Secure User Registration
- User Login
- Password Hashing
- Forgot Password

---

### 🤖 Disaster Prediction

- Predicts disaster risk using a trained Machine Learning model
- Uses:
  - 🌡 Temperature
  - 💧 Humidity
  - 🌧 Rainfall
  - 🌬 Wind Speed
- Displays Disaster Risk Level

---

### 🌦 Live Weather

- Real-time Weather
- Temperature
- Humidity
- Rainfall
- Wind Speed
- Weather Description
- Powered by OpenWeather API

---

### 📍 Safe Zone Navigation

- Google Maps Integration
- Nearby Hospitals
- Police Stations
- Fire Stations
- Emergency Services

---

### 🚨 Emergency Module

- National Emergency Numbers
- Quick Access Contacts
- Disaster Safety Tips

---

### 📊 Dashboard

- Personalized Dashboard
- Weather Summary
- Disaster Prediction Access
- Emergency Navigation

---

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Database | PostgreSQL |
| Machine Learning | Scikit-learn |
| API | OpenWeather API |
| Maps | Google Maps |
| Authentication | Werkzeug Security |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
Smart-Disaster-Management-System
│
├── app.py
├── README.md
├── LICENSE
├── requirements.txt
├── database.sql
├── .gitignore
│
├── models/
│   ├── disaster_model.pkl
│   └── train_model.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── prediction.html
│   ├── emergency.html
│   ├── map.html
│   └── admin.html
│
└── screenshots/
```

---

# 🔄 Project Workflow

```text
                 User Login
                      │
                      ▼
                Flask Backend
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
OpenWeather API   ML Prediction   PostgreSQL
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 Dashboard
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Safe Zone Map          Emergency Module
```

---

# 📈 Key Functionalities

✅ User Authentication

✅ Live Weather Monitoring

✅ Machine Learning Disaster Prediction

✅ Dashboard Analytics

✅ Google Maps Safe Zone

✅ Emergency Contact System

✅ PostgreSQL Database

✅ Responsive Bootstrap UI

✅ Secure Password Encryption

✅ GitHub Version Control
---

# 📸 Application Screenshots

> **Note:** Replace these placeholder images with screenshots from your application after creating the `screenshots` folder.

---

## 🏠 Home Page

![Home Page](screenshots/home.png)

The landing page introduces the Smart Disaster Management System and provides quick navigation to user authentication.

---

## 🔐 Login Page

![Login Page](screenshots/login.png)

Secure login page for registered users with encrypted password authentication.

---

## 📝 Registration Page

![Registration Page](screenshots/register.png)

Allows new users to create an account securely.

---

## 📊 Dashboard

![Dashboard](screenshots/dashboard.png)

Displays weather information and provides quick access to all project modules.

---

## 🤖 Disaster Prediction

![Prediction](screenshots/prediction.png)

Predicts disaster risk using Machine Learning based on:

- 🌡 Temperature
- 💧 Humidity
- 🌧 Rainfall
- 🌬 Wind Speed

---

## 📍 Safe Zone Map

![Map](screenshots/safezone.png)

Google Maps integration to locate nearby:

- 🏥 Hospitals
- 🚓 Police Stations
- 🚒 Fire Stations

---

## 🚨 Emergency Module

![Emergency](screenshots/emergency.png)

Provides emergency contact numbers and disaster safety guidelines.

---

# 🏗️ System Architecture

```text
                    +-----------------------+
                    |      User Browser     |
                    +----------+------------+
                               |
                               |
                      HTTP Requests
                               |
                               ▼
                    +-----------------------+
                    |     Flask Backend     |
                    +----------+------------+
                               |
         +---------------------+----------------------+
         |                     |                      |
         ▼                     ▼                      ▼
+----------------+   +------------------+   +------------------+
| OpenWeather API|   | Machine Learning |   | PostgreSQL DB    |
+----------------+   +------------------+   +------------------+
         |                     |                      |
         +---------------------+----------------------+
                               |
                               ▼
                    +-----------------------+
                    |  Disaster Prediction  |
                    +----------+------------+
                               |
                               ▼
                    +-----------------------+
                    | Dashboard & UI Pages  |
                    +-----------------------+
```

---

# 🤖 Machine Learning Workflow

```text
Weather Data
     │
     ▼
Temperature
Humidity
Rainfall
Wind Speed
     │
     ▼
Data Preprocessing
     │
     ▼
Trained ML Model (.pkl)
     │
     ▼
Prediction
     │
     ▼
Risk Level Displayed to User
```

---

# 🌦 Weather API Workflow

```text
OpenWeather API
        │
        ▼
Live Weather JSON
        │
        ▼
Flask Backend
        │
        ▼
Dashboard
Prediction Page
```

---

# 🗄️ Database Design

## Users Table

| Column | Type |
|---------|------|
| id | SERIAL |
| fullname | VARCHAR |
| email | VARCHAR |
| password | TEXT |

---

## Predictions Table

| Column | Type |
|---------|------|
| id | SERIAL |
| temperature | FLOAT |
| humidity | FLOAT |
| rainfall | FLOAT |
| wind | FLOAT |
| result | VARCHAR |
| created_at | TIMESTAMP |
---

# ⚙️ Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Rucha-Girme/Smart-Disaster-Management-System.git
```

```bash
cd Smart-Disaster-Management-System
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

**Command Prompt**

```bash
venv\Scripts\activate
```

**PowerShell**

```powershell
venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a file named:

```text
.env
```

Add the following variables:

```env
DB_HOST=localhost
DB_NAME=smart_disaster
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432

OPENWEATHER_API_KEY=your_api_key
```

> **Important:** Never upload your `.env` file to GitHub. Keep it listed in `.gitignore`.

---

## 5️⃣ Setup PostgreSQL

Create a PostgreSQL database:

```
smart_disaster
```

Import your SQL script to create the required tables.

---

## 6️⃣ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 📌 Future Scope

This project can be enhanced with:

- 🔔 Automatic Disaster Notifications
- 📱 Mobile Application
- 🌍 Multi-language Support
- 🤖 AI Chatbot for Emergency Guidance
- 📡 IoT Sensor Integration
- 📈 Advanced Analytics Dashboard
- ☁️ Cloud Deployment
- 📍 GPS-Based Safe Route Navigation
- 🚁 Disaster Relief Tracking
- 📲 SMS & Email Alert System

---

# 🎯 Learning Outcomes

Through this project, I gained experience in:

- Python Programming
- Flask Web Development
- Machine Learning Integration
- PostgreSQL Database Management
- REST API Integration
- Google Maps API
- Responsive UI Design
- Git & GitHub Version Control
- Full Stack Web Development

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 👩‍💻 Author

**Rucha Girme**

🎓 B.Sc. Computer Science Student

🌍 Interested in Artificial Intelligence, Machine Learning, and Data Analytics

GitHub:
https://github.com/Rucha-Girme

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

<div align="center">

## ⭐ Thank You for Visiting ⭐

**Smart Disaster Management System**

Built using Flask, Machine Learning, PostgreSQL, OpenWeather API, and Google Maps.

</div>
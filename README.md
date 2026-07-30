# 🌍 Smart Disaster Management System

A web-based **Smart Disaster Management System** developed using **Flask**, **Machine Learning**, **PostgreSQL**, **OpenWeather API**, and **Google Maps**. The application predicts disaster risk based on weather conditions and helps users access emergency services and nearby safe locations.

---

## 📌 Project Overview

Natural disasters such as floods, cyclones, and heatwaves can cause significant damage. This system assists users by:

- Predicting disaster risk using a Machine Learning model.
- Displaying live weather information.
- Showing nearby hospitals and emergency locations using Google Maps.
- Providing emergency contact numbers.
- Maintaining prediction history for analysis.

---

## ✨ Features

- 🔐 User Registration & Login
- 🔒 Secure Password Hashing
- 🔑 Forgot Password
- 🌦 Live Weather using OpenWeather API
- 🤖 Machine Learning Disaster Prediction
- 📊 Prediction History
- 📍 Google Maps Safe Zone
- 🚨 Emergency Contact Page
- 📱 Responsive Bootstrap Interface
- 🗄 PostgreSQL Database Integration

---

## 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| PostgreSQL | Database |
| Scikit-learn | Machine Learning |
| Bootstrap 5 | User Interface |
| HTML/CSS | Frontend |
| OpenWeather API | Live Weather Data |
| Google Maps | Safe Zone Map |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```text
Smart-Disaster-Management-System
│
├── app.py
├── README.md
├── requirements.txt
├── database.sql
├── .gitignore
│
├── models/
│   └── disaster_model.pkl
│
├── static/
│
├── templates/
│
└── screenshots/
```

---

## 📸 Screenshots

The repository contains screenshots of:

- 🏠 Home Page
- 🔑 Login Page
- 📊 Dashboard
- 🤖 Prediction Page
- 🗺 Safe Zone Map
- 🚨 Emergency Page

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Disaster-Management-System.git
```

### Open Project

```bash
cd Smart-Disaster-Management-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```text
DB_HOST=localhost
DB_NAME=smart_disaster
DB_USER=postgres
DB_PASSWORD=YOUR_PASSWORD
DB_PORT=5432
OPENWEATHER_API_KEY=YOUR_API_KEY
```

### Run the Application

```bash
python app.py
```

---

## 🔮 Future Enhancements

- 📲 Mobile Application
- 📈 Analytics Dashboard
- 🌍 Multi-city Weather Monitoring
- 📡 IoT Sensor Integration
- ☁ Cloud Deployment

---

## 👨‍💻 Author

Developed as a B.Sc. Computer Science Project using Flask and Machine Learning.

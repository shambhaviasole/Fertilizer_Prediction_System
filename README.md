# 🌱 Fertilizer Prediction System

## 📌 Overview

The **Fertilizer Prediction System** is an **AI-powered web application** that recommends the most suitable fertilizer based on soil properties, crop type, and environmental conditions. The goal of this project is to assist farmers and agricultural organizations in optimizing fertilizer usage, improving crop yield, and promoting sustainable farming practices.

The system integrates a **machine learning model** with a **Django-based web interface**, providing predictions through a clean and interactive dashboard.

---

## 🎯 Objectives

* To help farmers **choose the right fertilizer** for specific crops.
* To **minimize overuse or misuse** of fertilizers.
* To **increase crop productivity** and **reduce costs**.
* To **leverage AI in agriculture** for smarter decision-making.

---

## 🚀 Key Features

✅ **User Authentication:** Secure login for admins and users (farmers).
✅ **Interactive Dashboard:** Displays predictions, soil data, and recommendations.
✅ **AI-Powered Predictions:** ML model trained on soil nutrients and crop data.
✅ **Responsive UI:** Designed with a modern color palette (`#0a0f1f, #007bff, #00eaff, #00ff66, #2aa6ff, #ffffff`).
✅ **Database Integration:** Supports MySQL/SQLite for user and crop data management.
✅ **Scalable Design:** Easy to extend with new features like crop yield prediction, weather integration, etc.

---

## 🏗️ Tech Stack

**Frontend:**

* HTML5, CSS3, JavaScript

**Backend:**

* Django (Python Framework)

**Machine Learning:**

* Scikit-learn
* Pandas, NumPy
* Joblib (for saving/loading model)

**Database:**

* SQLite (default) / MySQL

**Others:**

* Bootstrap / Custom CSS for styling

---

## 📂 Project Structure

```
FertilizerPredictionSystem/
│── FertilizerPredictionSystem/      # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
│── prediction_app/                  # Main Django app
│   ├── migrations/                  # Database migrations
│   ├── templates/                   # HTML Templates (Dashboard, Forms, etc.)
│   ├── static/                      # CSS, JS, Images
│   ├── views.py                     # Backend logic
│   ├── models.py                    # Database models
│   ├── urls.py                      # App routes
│
│── models/                          # Machine Learning models
│   └── Fertilizer_Prediction.joblib
│
│── requirements.txt                 # Python dependencies
│── manage.py                        # Django management script
│── README.md                        # Project documentation
```

---

## ⚙️ Installation & Setup

### 🔹 Prerequisites

* Python 3.8+
* pip (Python package manager)
* Virtual Environment (recommended)
* MySQL/SQLite

### 🔹 Steps to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/fertilizer-prediction-system.git
cd fertilizer-prediction-system
```

2. **Create and Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Database Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the Development Server**

```bash
python manage.py runserver
```

6. **Access the Application**
   Go to → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


---

## 📂 Downdjango>=4.2
djangorestframework>=3.14
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0
joblib>=1.3.0
mysqlclient>=2.2.0
gunicorn>=21.2.0
whitenoise>=6.5.0
[requirements.txt](https://github.com/user-attachments/files/22056816/requirements.txt)
load requirements.txt

It includes:

* Django (backend framework)
* Django REST Framework (if you extend with APIs)
* Pandas, NumPy (data handling)
* Scikit-learn, Joblib (ML model)
* MySQLclient (database connector)
*Gunicorn, Whitenoise (for deployment)

---

## 📊 Machine Learning Model Details

* **Input Features:**

  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * Temperature
  * Humidity
  * Moisture
  * Crop Type

* **Algorithm Used:**

  * Classification model (Scikit-learn) trained on agricultural dataset

* **Output:**

  * Recommended fertilizer (e.g., Urea, DAP, 14-35-14, 28-28, etc.)

* **Model Storage:**

  * Saved as `Fertilizer_Prediction.joblib` for faster loading

---

## 📸 Demo Video

https://github.com/user-attachments/assets/38f302a5-aa62-4bcb-99df-1511e130ed9e

* 🏠 Homepage
* 📊 Dashboard
* 🌾 Fertilizer Prediction Page
* 🤖 AI Chatbot
* 🌦️ Live Weather

---

## 🛠️ Future Enhancements

* 🔮 **Crop Yield Prediction** based on soil & weather data.
* ☁️ **Weather API Integration** for real-time recommendations.
* 📱 **Mobile App Version** for farmers.
* 🌍 **Multilingual Support** (English, Hindi, etc.).
* 📈 **Visualization Dashboard** for insights and analytics.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit changes
4. Submit a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software for personal and educational purposes.

---



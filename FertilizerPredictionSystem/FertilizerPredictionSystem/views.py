from django.shortcuts import render, redirect
import pymysql
from django.contrib.auth.hashers import make_password, check_password
import joblib
import pandas as pd
from django.conf import settings
import os

# Load model once
MODEL_PATH = os.path.join(settings.BASE_DIR, "FertilizerPredictionSystem", "models", "Fertilizer_Prediction.joblib")
model = joblib.load(MODEL_PATH)

MODEL_PATH = os.path.join(
    settings.BASE_DIR,
    "FertilizerPredictionSystem",
    "models",
    "Fertilizer_Prediction.joblib"
)
model = joblib.load(MODEL_PATH)




# ---------- HOME PAGE ----------
def homepage(request):
    return render(request, "index.html")


# ---------- REGISTER ----------
def register(request):
    msg = ""
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        if password != confirm_password:
            msg = "Passwords do not match!"
            return render(request, 'register.html', {'message': msg})

        con = None   # 🔑 initialize connection
        try:
            con = pymysql.connect(
                host='mysql-shambhavi-shambhaviasole9-python.h.aivencloud.com',
                port=10850,
                user='shambhavi',
                password='AVNS_HmvZ_bGZzAhYDISIpxY',
                database='FertilizerPredictionDB',
                ssl={'ssl': {}}
            )
            curs = con.cursor()

            # check if email exists
            check_query = "SELECT email FROM users WHERE email=%s"
            curs.execute(check_query, (email,))
            if curs.fetchone():
                msg = "Email already registered!"
                return render(request, 'register.html', {'message': msg})

            # insert user with hashed password
            hashed_password = make_password(password)
            insert_query = """
                INSERT INTO users (full_name, email, password) 
                VALUES (%s, %s, %s)
            """
            curs.execute(insert_query, (name, email, hashed_password))
            con.commit()

            return render(request, 'login.html', {'message': "Registration successful! Please login."})

        except Exception as e:
            msg = f"Error: {e}"

        finally:
            if con:   # 🔑 close only if connection exists
                con.close()

    return render(request, 'register.html', {'message': msg})



# ---------- LOGIN ----------
def loginpage(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip()
        psw = request.POST.get('password', '').strip()

        try:
            con = pymysql.connect(
                host='mysql-shambhavi-shambhaviasole9-python.h.aivencloud.com',
                port=10850,
                user='shambhavi',
                password='AVNS_HmvZ_bGZzAhYDISIpxY',
                database='FertilizerPredictionDB',
                ssl={'ssl': {}}
            )
            curs = con.cursor()

            # get user by email
            query = "SELECT user_id, password FROM users WHERE email = %s"
            curs.execute(query, (email,))
            result = curs.fetchone()

            if result and check_password(psw, result[1]):
                request.session['user_id'] = result[0]
                return redirect('dashboard')
            else:
                return render(request, 'loginfail.html', {'message': 'Invalid credentials'})

        except Exception as e:
            return render(request, 'loginfail.html', {'error': str(e)})

        finally:
            con.close()

    return render(request, 'login.html')


# ---------- LOGIN FAIL ----------
def loginfail(request):
    return render(request, "loginfail.html")


# ---------- DASHBOARD ----------
def dashboard(request):
    # Ensure only logged-in users can access
    if 'user_id' not in request.session:
        return redirect('login')
    return render(request, 'dashboard.html')


# fertilizer prediction


def fertilizer_prediction(request):
    if request.method == "POST":
        try:
            newdata = {
                'Temparature': [float(request.POST.get('Temparature'))],
                'Humidity': [float(request.POST.get('Humidity'))],   # keep space if dataset has it
                'Moisture': [float(request.POST.get('Moisture'))],
                'Soil_Type': [int(request.POST.get('Soil_Type'))],
                'Crop_Type': [int(request.POST.get('Crop_Type'))],
                'Nitrogen': [float(request.POST.get('Nitrogen'))],
                'Potassium': [float(request.POST.get('Potassium'))],
                'Phosphorous': [float(request.POST.get('Phosphorous'))],
            }

            df = pd.DataFrame(newdata)
            pred = model.predict(df)
            prediction = pred[0]   # Fertilizer name

            # Save result in session and redirect
            request.session['fertilizer_result'] = prediction
            return redirect('fertilizer_result')

        except Exception as e:
            request.session['fertilizer_result'] = f"Error during prediction: {str(e)}"
            return redirect('fertilizer_result')

    return render(request, "fertilizer_prediction.html")


def fertilizer_result(request):
    prediction = request.session.get('fertilizer_result', None)
    return render(request, "fertilizer_result.html", {'prediction': prediction})




# ---------- LOGOUT ----------
def logout(request):
    # Clear the session
    request.session.flush()   # removes all session data
    
    # Option 1 → Show logout.html confirmation page
    return render(request, "logout.html")

    # Option 2 → If you just want redirect (skip logout page):
    # return redirect('login')

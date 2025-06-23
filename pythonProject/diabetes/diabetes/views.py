import os
import pickle
from django.shortcuts import render
from django.conf import settings

# Model ko load karna
model_path = os.path.join(settings.BASE_DIR, 'diabetes_model.pkl')

with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Home page view
def home(request):
    return render(request, "home.html")

# Prediction form view
def predict(request):
    return render(request, "predict.html")

# Prediction result view
def result(request):
    try:
        # Get user inputs
        val1 = float(request.GET['n1'])
        val2 = float(request.GET['n2'])
        val3 = float(request.GET['n3'])
        val4 = float(request.GET['n4'])
        val5 = float(request.GET['n5'])
        val6 = float(request.GET['n6'])
        val7 = float(request.GET['n7'])
        val8 = float(request.GET['n8'])

        # Predict the outcome using the trained model
        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

        # Display result based on prediction
        result1 = "Positive" if pred[0] == 1 else "Negative"
    except Exception as e:
        result1 = f"Error: {e}"

    # Render the result in the template
    return render(request, "predict.html", {"result2": result1})

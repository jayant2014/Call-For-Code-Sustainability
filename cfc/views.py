from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import context

from .forms import ImageUploadForm
from .forms import SignUpForm

from tensorflow.keras.preprocessing import image
import os
import numpy as np
from tensorflow.keras.models import load_model

class_names = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'green-glass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if a user with the given email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'A user with this email address already exists.')
            else:
                user = form.save()  # This saves the user data to the database
                messages.success(request, 'Welcome! Your account has been created successfully.')
                login(request, user)  # Log the user in after successful signup
                return redirect('home')  # Redirect to the home page after signup
        else:
            # If form is not valid, display specific error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import authenticate, login
from django.contrib import messages



from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        # Check if the user already exists in the database
        user = User.objects.filter(email=email).first()

        if user:
            # If the user exists, authenticate and log them in
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')  # Redirect to the home page upon successful login
            else:
                return render(request, 'registration/login.html', {'error_message': 'Invalid email or password. Please try again.'})
        else:
            # If the user does not exist, create a new user and log them in
            new_user = User.objects.create_user(username=email, email=email, password=password)
            login(request, new_user)
            return redirect('home')  # Redirect to the home page upon successful registration

    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'registration/home.html')


from .forms import ImageUploadForm

from django.contrib import messages

import os
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import ImageUploadForm

from django.shortcuts import render, redirect
from .forms import ImageUploadForm

import os
from django.conf import settings
from django.http import JsonResponse

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        file_name = uploaded_file.name

        # Save the uploaded file to the 'uploads' folder
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        with open(file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)


        return redirect('success_template')
    else:
        return redirect('home')

# views.py
from django.shortcuts import render
from .forms import WasteDataForm

emission_factors = {
    'plastic': 0.1,  # Example emission factors for different waste types
    'paper': 0.05,
    'metal': 0.2
    # Add more emission factors for other waste types as needed
}

def predict_class(request):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize the image

    model1 = load_model("ws_new.keras")
    print(predict(image_path, model1))
    # Make predictions
    predictions = model1.predict(img)

    # Get the class with the highest probability
    predicted_class = np.argmax(predictions)
    predicted_class_name = class_names[predicted_class]
    return render(request, 'result.html', predicted_class_name)

def calculate(request):
    if request.method == 'POST':
        form = WasteDataForm(request.POST)
        if form.is_valid():
            waste_data = {}
            total_emissions = 0
            for waste_type, emission_factor in emission_factors.items():
                quantity = form.cleaned_data.get(waste_type, 0)
                waste_data[waste_type] = quantity
                emissions = emission_factor * quantity
                total_emissions += emissions
            return render(request, 'registration/result.html', {'waste_data': waste_data, 'total_emissions': total_emissions})
    else:
        form = WasteDataForm()

    return render(request, 'registration/result.html', {'form': form})


def calculate_credit(request):
    # Handle credit calculation logic here
    # ...

    return redirect('calculate')


def logout_view(request):
    # Logout logic here
    # ...
    return redirect('signup')  # Assuming you have a URL pattern named 'signup'.


# views.py
from django.shortcuts import render
from .models import CarbonCredit
from .forms import CarbonCreditForm

def user_carbon_credits(request):
    if request.method == 'POST':
        form = CarbonCreditForm(request.POST)
        if form.is_valid():
            credits = form.cleaned_data['credits']
            # Get the current user
            user = request.user
            # Update or create carbon credit data for the user
            carbon_credit, created = CarbonCredit.objects.get_or_create(user=user)
            carbon_credit.credits += credits
            carbon_credit.save()
            return render(request, 'registration/success_template.html', {'message': 'Carbon credits updated successfully!'})
    else:
        form = CarbonCreditForm()
    return render(request, 'registration/carbon_credit_form.html', {'form': form})

from rest_framework.views import APIView
from rest_framework.response import Response


image_path = "paper15.jpg"
class_names = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 'green-glass', 'metal', 'paper', 'plastic', 'shoes', 'trash', 'white-glass']
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import json
def predict_class(request):
    return redirect('home')

from django.shortcuts import render

from django.shortcuts import render

def user_profile(request):

    context = {
        # 'user_info': "Amit Saxena",
        'carbon_credits': 100,
    }

    return render(request, 'registration/user_profile.html', user_carbon_credits)


def user_trade(request):
    return render(request, 'registration/home.html')

def success_template(request):
    return render(request, 'registration/success_template.html')






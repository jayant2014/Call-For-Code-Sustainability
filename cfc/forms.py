from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Enter a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# class ImageUploadForm(forms.Form):
#     image = forms.ImageField()

class CombinedUploadForm(forms.Form):
    image = forms.ImageField()

class WasteDataForm(forms.Form):
    plastic = forms.FloatField(required=False)
    paper = forms.FloatField(required=False)
    metal = forms.FloatField(required=False)


# forms.py
from django import forms

class CarbonCreditForm(forms.Form):
    credits = forms.IntegerField()
    # Add more form fields corresponding to your model fields



from django import forms
from .models import UploadedImage

from django import forms
from .models import UploadedImage

# imageupload/forms.py

from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image', )













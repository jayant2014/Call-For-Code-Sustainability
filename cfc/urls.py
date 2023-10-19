from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
#from .views import logout_view, upload_image, show_credits
from django.urls import path
# from .views import WastePredictor

urlpatterns = [
    path('', views.signup, name=''),       # URL for signup page
    path('home/', views.home, name='home'),  # URL for login page
    path('login/', views.login_view, name='login_view'),
    path('upload/', views.upload_image, name='upload_image'),
    path('calculate_credit/', views.calculate_credit, name='calculate_credit'),
    path('logout/', views.logout_view, name='logout'),
    path('calculate/', views.calculate, name='calculate'),
    path('user_carbon_credits/', views.user_carbon_credits, name='user_carbon_credits'),
    path('user_trade/', views.user_trade, name='user_trade'),
    path('profile/', views.user_profile, name='user_profile'),
    path('success_template/',views.success_template, name ='success_template'),
    path('predict_class/', views.predict_class, name='predict_class'),




]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static

# ... your other URL patterns ...

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from info_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('welcome/', views.welcome),
    path('goodbye/', views.goodbye),    
    path('current-time/', views.current_time),
    path('greet/', views.greet),
    path('age-category/', views.age_category),
    path('sum/<num1>/<num2>', views.sum_view),



]

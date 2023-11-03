from django.urls import path
from main import views
print("that is for url")
urlpatterns = [
    path('',views.index,name='index'),
    path('userBipolar',views.userBipolar,name='userBipolar')
]
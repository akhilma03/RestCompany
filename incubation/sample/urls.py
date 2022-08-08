from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('',views.getRoutes,name="routes"),
    path ('users/register/',views.registerUser,name = "registerUser"),
    path('users/profile/<int:pk>/',views.getUserProfile,name="UserProfile"),
    path('users/',views.getUsers,name="Users"),
    path('application/',views.getApplication,name="Application"),
    path('appDetails/<str:pk>/',views.getApplicationDetails,name="ApplicationDetails"),
    path('application/register/',views.addApplication,name="addApplication"),
    path('appDetails/statusedit/<int:pk>/',views.StatusApplication,name="StatusApplication"),
    path('appDetails/deleteApplication/<int:pk>/',views.DeleteApplication,name="DeleteApplication"),



]

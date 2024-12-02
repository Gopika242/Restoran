from django.urls import path
from AdminApp import views
urlpatterns=[
 path('index/',views.index,name='index'),
 path('AddCuisine/',views.AddCuisine,name='AddCuisine'),
 path('SaveCuisine/', views.SaveCuisine, name='SaveCuisine'),
 path('DisplayCuisine/', views.DisplayCuisine, name='DisplayCuisine'),
 path('EditCuisine/<int:E_id>/', views.EditCuisine, name='EditCuisine'),
 path('UpdateCuisine/<int:U_id>/', views.UpdateCuisine, name='UpdateCuisine'),
 path('DeleteCuisine/<int:D_id>/', views.DeleteCuisine, name='DeleteCuisine'),

 path('AddDish/', views.AddDish, name='AddDish'),
 path('SaveDish/', views.SaveDish, name='SaveDish'),
 path('DisplayDish/', views.DisplayDish, name='DisplayDish'),
 path('EditDish/<int:Ed_id>/', views.EditDishes, name='EditDish'),
 path('UpdateDish/<int:UD_id>/', views.UpdateDish, name='UpdateDish'),
 path('DeleteDish/<int:DD_id>/', views.DeleteDish, name='DeleteDish'),

 path('Login/', views.Login, name='Login'),
 path('AdminLogin/', views.AdminLogin, name='AdminLogin'),
 path('AdminLogout/', views.admin_logout, name='AdminLogout'),
 path('ContactDetails/',views.ContactDetails,name='ContactDetails'),
 path('DeleteContact/<int:D>/', views.DeleteContact, name='DeleteContact'),




]

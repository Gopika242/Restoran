from django.urls import path
from WebApp import views
urlpatterns=[
path('Home/',views.Home,name='Home'),
path('About/',views.About,name='About'),
path('Contact/',views.Contact,name='Contact'),
path('Menu/',views.Dishes,name='Menu'),
path('SaveContact/',views.SaveContact,name='SaveContact'),
path('DishesFiltered/<CName>/',views.DishesFiltered,name='DishesFiltered'),
path('SingleDish/<int:Di>',views.SingleDish,name='SingleDish'),
path('SignUp/',views.SignUp,name='SignUp'),
path('SaveSignUp/',views.SaveSignUp,name='SaveSignUp'),
path('SignIn/',views.SignIn,name='SignIn'),
path('UserLogin/',views.UserLogin,name='UserLogin'),
path('UserLogout/',views.UserLogout,name='UserLogout'),
path('SaveCart/',views.CartSave,name='SaveCart'),
path('CartsPage/',views.CartsPage,name='CartsPage'),
path('Checkout/',views.Checkout,name='Checkout'),
path('CartRemove/<int:D_id>/',views.CartRemove,name='CartRemove'),
path('OrderSave/',views.OrderSave,name='OrderSave'),
path('Payment/',views.Payment,name='Payment'),
]
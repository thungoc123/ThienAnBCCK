from django.urls import path
from.import views
urlpatterns = [
    path('', views.Home, name="home" ),
    path('search',views.Search,name="search"),
    path('comment',views.Addcomment,name="comment"),
    path('signup',views.Signup,name="signup"),
    path('signin',views.Signin,name="signin"),
    path('logout',views.Logout,name="Logout"),
    path('<slug:slug>',views.Detail,name="detail"),
   
]
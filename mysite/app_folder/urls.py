from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),
    # path('login/', LoginView.as_view(
    #     redirect_authenticated_user=True,
    #     template_name='app_folder/login.html'
    # ), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]

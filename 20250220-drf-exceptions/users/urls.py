from django.urls import path

from users.views import LoginView, LogoutView, SignupView, UserDetailView, UserListView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/", UserDetailView.as_view(), name="user_detail"),
    path("users/", UserListView.as_view(), name="user_list"),
]

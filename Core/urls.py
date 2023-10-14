from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from . import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("detail/", views.Detail, name="Detail"),
    path("logout/", views.Logout_user, name="Logout"),
    path("signin/", views.Register, name="Register"),
    path("delete/", views.Delete, name="Delete"),
    path("update/", views.Update, name="Update"),
    path("update/changepassword/", views.UpdatePassword, name="UpdatePassword"),
    path(
        "reset-password/",
        PasswordResetView.as_view(template_name="ResetPassword.html"),
        name="reset_password",
    ),
    path(
        "reset-password-done/",
        PasswordResetDoneView.as_view(template_name="ResetPasswordDone.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(template_name="ResetPasswordConfirm.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset-password-complete/",
        PasswordResetCompleteView.as_view(template_name="ResetPasswordComplete.html"),
        name="password_reset_complete",
    ),
]

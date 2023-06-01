from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('signup/', views.UserRegistrationView.as_view(), name='user_register'),
    path('verify/', views.UserVerifyCodeView.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('get-user/', views.GetUser.as_view(), name='get_user'),
    path('update-user/', views.UpdateUser.as_view(), name='update_user'),
    path('bookmark-plant/<int:id_plant>', views.AddBookmark.as_view(), name='save_plant'),
    path('bookmark-plant/', views.GetBookmarkList.as_view(), name='saved_plant_list'),
    path('update-GardenOwner/', views.UpdateGardenOwner.as_view(), name='update_FardenOwner'),
    path('set_default_condition/', views.UserSetDefaultConditionView.as_view(), name='set_default_condition'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
]

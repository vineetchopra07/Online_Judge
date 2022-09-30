from django.urls import path

from . import views

app_name = 'OJ'

urlpatterns = [
    path('problems/',views.problems, name='problem'),
    path('problem/<str:question_name>',views.problem_details,name='problem_details'),
    path("register", views.register_request, name="register"),
    path("login",views.login_request,name="login"),
    path('leaderboard',views.user_submission,name='user_submission'),
    path('',views.user_logout,name='logout'),
]
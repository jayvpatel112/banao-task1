from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('post/all/', views.allpost, name='all-posts'),
    path('draft/', views.draft, name='draft'),
    path('appoinmentconfirm/<int:id>', views.appoinmentconfirm, name='appoinmentconfirm'),
    path('finalconfirm/<int:id>', views.finalconfirm, name='finalconfirm'),
    path('bookslotdashboard/', views.bookslotdashboard, name='bookslotdashboard')
]
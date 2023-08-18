"""atm_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from atm_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    # # path('reg_dash',views.reg_dash,name='reg_dash'),
    path('deposit<int:id>',views.deposit,name='deposit'),
    path('withdraw<int:id>',views.withdraw,name='withdraw'),
    path('w_btn',views.w_btn,name='w_btn'),
    path('d_dash',views.d_dash,name='d_dash'),
    path('balance<int:id>',views.balance,name='balance'),
    path('history<int:id>',views.history,name='history'),
    path('logout', views.logout,name='logout'),
]

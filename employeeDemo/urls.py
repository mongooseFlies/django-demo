"""employeeDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from employee.views import employee_listing, signup, account_view, account_edit, update_password
from django.contrib.auth.views import *

urlpatterns = [
    re_path(r'^signup/$', signup, name='signup'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^account/$', account_view, name='account_view'),
    re_path(r'^account/edit$', account_edit, name='account_edit'),
    re_path(r'^account/edit/password$', update_password, name='update_password'),
    re_path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', PasswordResetConfirmView.as_view(), {'template_name' : 'registration/Forgot_password.html'}, name='password_reset_confirm'),
    re_path(r'^password_reset/$', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    re_path(r'^password_reset/done/$',PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$',PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
    re_path(r'^$', employee_listing, name='employee_listing'),

]

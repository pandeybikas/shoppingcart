from django.urls import path
from . import views
from .forms import PasswordForm
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('signup', views.signup, name='signup'),
    
    path('signin', views.signin, name='signin'),
    
    path('signout', views.signout, name='signout'),
    
    path('profile', views.profilePage, name='profile'),
    
    path('address', views.address, name='address'),

    path('passwordchange', auth_view.PasswordChangeView.as_view(template_name = 'app/changepassword.html', 
                                form_class = PasswordForm, success_url= 'passwordchangedone'
    ), name= 'passwordchange'),

    path('passwordchangedone', auth_view.PasswordChangeDoneView.as_view(
        template_name = 'app/passwordchangedone.html'
    ), name='passwordchangedone')
]

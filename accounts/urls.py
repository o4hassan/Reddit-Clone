
from django.conf.urls import url
from . import views

app_name ='accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name="signup"),
    url(r'^login/', views.loginview, name="login"),
    url(r'^logout/', views.logoutview, name="logout"),
    url(r'^profile/', views.profile, name="profile"),
    url(r'^edit/(?P<user_id>[0-9]+)/$', views.edit, name ="edit")
]



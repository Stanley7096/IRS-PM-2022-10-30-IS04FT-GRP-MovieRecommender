from django.conf.urls import url
from . import views
from django.conf.urls import static



app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^showmessage/', views.showmessage, name='showmessage'),

    url(r'^index/',views.index,name='index'),

]

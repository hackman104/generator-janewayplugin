from django.conf.urls import url
from plugins.<%= dirName %> import views

urlpatterns = [
    url(r'^$/', views.index, name='<%= managerUrl %>'),
    # declare further URLS here   
]
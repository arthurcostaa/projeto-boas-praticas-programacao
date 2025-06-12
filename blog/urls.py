from django.urls import path

from blog.views import home, blog, sobre

urlpatterns = [
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('sobre/', sobre, name='sobre'),

]

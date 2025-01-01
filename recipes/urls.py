from django.urls import path
from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),
    path('sobre/', sobre, name='sobre'),
]
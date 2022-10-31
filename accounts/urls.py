from django.urls import path

from .views import getUser, login, register, update_user, delete

urlpatterns = [
    #path('us', getUser, name='user'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('update', update_user, name='update'),
    path('delete', delete, name='delete')
]
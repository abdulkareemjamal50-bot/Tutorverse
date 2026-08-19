from django.urls import path
from . import views


urlpatterns = [

    path(
        'conversation/<int:user_id>/',
        views.conversation,
        name='conversation'
    ),

    path(
        'inbox/',
        views.inbox,
        name='inbox'
    ),

]
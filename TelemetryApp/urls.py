from django.urls import path
from .views import home, project, gallery,get_variablesa, loginUser, logoutUser, telemetry

urlpatterns = [
    path('', home, name='home'),
    path('project', project, name='project' ),
    path('gallery', gallery, name='gallery' ),
    path('login', loginUser, name='login' ),
    path('logout', logoutUser, name='logout' ),
    path('telemetry', telemetry, name='telemetry' ),
    path('ajax', get_variablesa, name="getvalores" ),
]
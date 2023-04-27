from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = 'movieapp'
urlpatterns = [

    path('', index, name='index'),
    path('movie/<int:movie_id>/', detail, name='detail'),
    path('add/', add_movie, name='add_movie'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

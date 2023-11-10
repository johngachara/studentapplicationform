from django.conf.urls.static import static
from django.urls import path

from Emobilisproject import settings
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('all/',views.all_students,name='allstudents'),
    path('student/<int:stud_id>',views.student,name='student')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
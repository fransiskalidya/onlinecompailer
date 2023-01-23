from django.urls import path

from . import views

urlpatterns = [
    path('run', views.index, name='index'),
    path('test_files', views.get_test_file_list, name='get_test_file_list'),
    path('test_file/upload', views.upload_java_test_file, name='upload_java_test_file'),
    path('test_file/delete', views.delete_test, name='delete_test_file')
]

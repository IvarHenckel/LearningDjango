from django.urls import path
from .views import (
    CourseListView,
    CourseView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
    #my_fbv
)

app_name = 'courses'
urlpatterns = [
    #path('', my_fbv, name='courses-list')
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('list/', CourseListView.as_view(), name='courses-list-again'),
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('update/<int:id>/', CourseUpdateView.as_view(), name='courses-update'),
    path('delete/<int:id>/', CourseDeleteView.as_view(), name='courses-delete'),
]
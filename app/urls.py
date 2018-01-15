from django.contrib import admin
from django.urls import path, re_path

from .views import index, course, question_and_answer

urlpatterns = [
    path('', index, name="index"),
    re_path('course(/(?P<c_name>\w+)?/)?', course, name="course"),
    path('Q&A/', question_and_answer),
]

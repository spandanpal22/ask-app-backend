from django.urls import path, include

from . import views

urlpatterns = [
    path('questions', views.QuestionView.as_view(), name='questionsGetPost'),
    path('questions/<int:pk>', views.QuestionView.as_view(), name='questionsPutDelete'),
    path('answers', views.AnswerView.as_view(), name='answersGetPost'),
    path('answers/<int:pk>', views.AnswerView.as_view(), name='answersPutDelete'),
    path('', views.Login, name='login'),

]

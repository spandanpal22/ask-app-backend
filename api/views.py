from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import QuestionSerializer,AnswerSerializer

from .models import Question,Answer

from .forms import LoginForm

def Login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
            return render(request, 'Thanks.html')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


"""
API Part Below
"""


class QuestionView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = Question.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        saved_question = get_object_or_404(Question.objects.all(), pk=pk)
        serializer = QuestionSerializer(saved_question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("put success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        question = get_object_or_404(Question.objects.all(), pk=pk)
        question.delete()
        return Response("delete success", status=204)



"""Test here"""
class AnswerView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_answer = get_object_or_404(Answer.objects.all(), pk=pk)
        serializer = AnswerSerializer(saved_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("put success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        answer = get_object_or_404(Answer.objects.all(), pk=pk)
        answer.delete()
        return Response("delete success", status=204)

"""
class AnswerView(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = AnswerSerializer(answers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("success", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_answer = get_object_or_404(Answer.objects.all(), pk=pk)
        serializer = AnswerSerializer(saved_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("put success")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        answer = get_object_or_404(Answer.objects.all(), pk=pk)
        answer.delete()
        return Response("delete success", status=204)
"""


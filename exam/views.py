from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category, Difficult, Question
from .serializers import (
        CategorySerializer, 
        DifficultSerializer, 
        # IncorectAnswerSerializer, 
        QuestionSerializer,
)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DifficultView(viewsets.ModelViewSet):
    queryset = Difficult.objects.all()
    serializer_class = DifficultSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
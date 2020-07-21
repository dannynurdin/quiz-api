from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Category, Difficult, Type, Question
from .serializers import (
        CategorySerializer, 
        DifficultSerializer, 
        TypeSerializer,
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

class TypeView(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
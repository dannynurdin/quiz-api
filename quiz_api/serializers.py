from rest_framework import serializers
from .models import Category, Difficult, Type, Question

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')

class DifficultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficult
        fields = ('id', 'url', 'name')

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'url', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'url', 'category', 'types', 'difficult', 'question',
                 'correct_answer', 'incorrect_answer')
from rest_framework import serializers
from .models import Category, Difficult, Question

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')

class DifficultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficult
        fields = ('id', 'url', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'url', 'category', 'difficult', 'name',
                 'corect_answer', 'incorect_answer_0', 'incorect_answer_1', 'incorect_answer_2')
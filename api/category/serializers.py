from rest_framework import serializers
from .models import Category
from ..study.serializers.study_sz import StudySerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'name', ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    study = StudySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_id', 'name', 'study', ]

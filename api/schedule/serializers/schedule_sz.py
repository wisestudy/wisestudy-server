from rest_framework import serializers
from ..models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    study_title = serializers.ReadOnlyField(source='study.title')

    class Meta:
        model = Schedule
        fields = ['schedule_id', 'study', 'study_title', 'datetime', 'place', 'title', 'description']
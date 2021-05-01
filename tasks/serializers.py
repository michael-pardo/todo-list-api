from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','name', 'description', 'created_at', 'updated_at', 'status')

    def create(self, validated_data):
        task = Task.objects.create(
            user=self.context['request'].user,
            **validated_data
        )
        return task

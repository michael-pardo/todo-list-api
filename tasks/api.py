from django.apps import apps
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        return {'request': self.request}


class CountView(RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    app = None
    model = None

    def retrieve(self, request, *args, **kwargs):
        model_class = apps.get_model(app_label=self.app, model_name=self.model)
        count = model_class.objects.count()

        return JsonResponse({'count': count})

from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .tasks import send_new_job_email     # Celery task 

# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


    # Send email alert when a job is created
    def perform_create(self,serializer):
        job = serializer.save()
        print("DJANGO: Job created, sending task...")
        send_new_job_email.delay(job.id) # call celery task



from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Job

@shared_task
def send_new_job_email(job_id):
    job = Job.objects.get(id=job_id)

    send_mail(
        subject=f"New Job Posted: {job.title}",
        message=f"""
        A new job has been posted.

        Title: {job.title}
        Company: {job.company}
        Location: {job.location}
        Description: {job.description}
        """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['lalitmendapara5@gmail.com'],
            fail_silently=False,

    )
    print ("Email sent for job :", job.title)

    

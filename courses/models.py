from django.db import models


class AccessRequirement(models.TextChoices):
    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email required"


class PublishStatus(models.TextChoices):
    PUBLISH = "publish", "Published"
    COMMING_SOON = "soon", "Comming Soon"
    DRAFT = "draft", "Draft"


def handle_upload(instance, filename):
    return f"{filename}"


class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    publish_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=handle_upload, blank=True, null=True)
    access = models.CharField(max_length=15, choices=AccessRequirement.choices, default=AccessRequirement.EMAIL_REQUIRED)
    status = models.CharField(max_length=10, choices=PublishStatus.choices, default=PublishStatus.DRAFT)


    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISH
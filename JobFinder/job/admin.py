from django.contrib import admin
from .models import Resume, JobPost, Match, User

# Register your models here.
admin.site.register(User)
admin.site.register(Resume)
admin.site.register(JobPost)
admin.site.register(Match)
from django.contrib import admin

from .models import Resume

# Register your models here.


@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','address','state','my_file','job_city']


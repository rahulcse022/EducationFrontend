from django.contrib import admin


from learningApp.models import AddCourse, BuyCourse

# Register your models here.

admin.site.register(AddCourse)
admin.site.register(BuyCourse)
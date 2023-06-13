from django.contrib import admin
from .models import Schedule, Instructors, Weekdays, Hours


admin.site.register(Schedule)
admin.site.register(Instructors)
admin.site.register(Weekdays)
admin.site.register(Hours)

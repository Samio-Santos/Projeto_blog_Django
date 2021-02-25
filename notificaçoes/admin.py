from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_from', 'user_to', 'text','date', 'is_seen')
    list_display_links = ('id', 'user_from', 'user_to')
    # readonly_fields = ['autor_post']
admin.site.register(Notification, NotificationAdmin)
from django.contrib import admin
from .models import Poll, Ses

# Register your models here.
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
	list_display = ['question', 'option_one', 'option_two', 'option_three', 'created', 'updated']

@admin.register(Ses)
class SesAdmin(admin.ModelAdmin):
	list_display = ['poll', 'ses', 'created']

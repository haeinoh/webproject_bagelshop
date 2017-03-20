from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Suggestion)
admin.site.register(Blog)
admin.site.register(comment)

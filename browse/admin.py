from django.contrib import admin
from .models import picture, category, browse_lang
# Register your models here.
admin.site.register(picture)
admin.site.register(category)
admin.site.register(browse_lang)
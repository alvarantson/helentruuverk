from django.contrib import admin
from navbar.models import contact, navbar_lang, langs, social_media

# Register your models here.
admin.site.register(contact)
admin.site.register(navbar_lang)
admin.site.register(langs)
admin.site.register(social_media)
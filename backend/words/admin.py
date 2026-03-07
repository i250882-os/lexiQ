from django.contrib import admin
from .models import Word, UserWord, Paragraph

admin.site.register(Word)
admin.site.register(UserWord)
admin.site.register(Paragraph)

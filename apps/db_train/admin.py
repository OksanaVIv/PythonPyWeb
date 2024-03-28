from django.contrib import admin

from django.contrib import admin
from .models import Author
from .models import AuthorProfile
from .models import Entry
from .models import Tag

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Entry)
admin.site.register(Tag)

# Зарегистрируйте свои модели в админ панели здесь

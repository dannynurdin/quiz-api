from django.contrib import admin
from .models import (
    Category,
    Type,
    Difficult,
    Question,
)


admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Difficult)
admin.site.register(Question)

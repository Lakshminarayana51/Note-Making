from django.contrib import admin
from apiapp.models import user_cred,todo_data # type: ignore
# Register your models here.

admin.site.register(user_cred)
admin.site.register(todo_data)
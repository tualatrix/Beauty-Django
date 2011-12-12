from django.contrib import admin
from usbeauty.facebook.models import facebook
from usbeauty.users.models import users

admin.site.register((facebook))
admin.site.register((users))
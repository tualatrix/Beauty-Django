from django.contrib import admin
from usbeauty.facebook.models import facebook
from usbeauty.users.models import users

class facebookAdmin(admin.ModelAdmin):
	list_display =('name','votes','rates','uploader')


admin.site.register((facebook,facebookAdmin))
admin.site.register((users))
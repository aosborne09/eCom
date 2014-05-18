from django.contrib import admin

from .models import Address, Profile

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
	class Meta:
		model = Address

admin.site.register(Address, AddressAdmin)

class ProfileAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile, ProfileAdmin)
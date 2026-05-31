from django.contrib import admin
from .models import Profile, IdType, AgeType, Personality, FosterParent, Species

# Register your models here.
admin.site.register(Profile)
admin.site.register(IdType)
admin.site.register(AgeType)
admin.site.register(Personality)
admin.site.register(FosterParent)
admin.site.register(Species)
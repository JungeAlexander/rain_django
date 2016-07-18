from django.contrib import admin
from .models import Interaction


class InteractionAdmin(admin.ModelAdmin):
    fields = ['views', 'entity1', 'entity2']

admin.site.register(Interaction, InteractionAdmin)

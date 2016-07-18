from django.contrib import admin
from .models import Interaction, RNA, RNAalias


class InteractionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['views']}),
        ('Interacting entities', {'fields': ['entity1', 'entity2']}),
    ]

admin.site.register(Interaction, InteractionAdmin)
admin.site.register(RNA)
admin.site.register(RNAalias)

from django.contrib import admin
from .models import Interaction, RNA, RNAalias


class InteractionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['views']}),
        ('Interacting entities', {'fields': ['entity1', 'entity2']}),
    ]


class RNAaliasInline(admin.TabularInline):
    model = RNAalias
    extra = 3


class RNAAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['identifier', 'views']}),
        ('Description',      {'fields': ['description'], 'classes': ['collapse']}),
    ]
    inlines = [RNAaliasInline]
    list_display = ('identifier', 'description', 'is_mirna')
    list_filter = ['views', 'identifier']
    search_fields = ['description']

admin.site.register(Interaction, InteractionAdmin)
admin.site.register(RNA, RNAAdmin)
# admin.site.register(RNAalias)

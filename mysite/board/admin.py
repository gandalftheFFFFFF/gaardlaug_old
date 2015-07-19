from django.contrib import admin

from .models import BoardMember, Role, Cadastre
# Register your models here.

class RolesInLine(admin.StackedInline):
    model = Role
    extra = 0


class BoardMemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Dates', {'fields': ['from_date', 'to_date']}),
        ('Street', {'fields': ['street_name', 'street_number', 'street_number_letter']}),
        ('Activity', {'fields': ['active']}),
    ]
    inlines = [RolesInLine]
    list_display = ('last_name', 'first_name', 'street_name')
    list_filter = (
        ('active', admin.BooleanFieldListFilter),
    )


admin.site.register(BoardMember, BoardMemberAdmin)
admin.site.register(Cadastre)
admin.site.register(Role)

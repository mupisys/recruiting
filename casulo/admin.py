from django.contrib import admin
from .models import Mensagem, Service, ServiceCategory, TeamMember
from django.utils.html import format_html
from django.templatetags.static import static

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio', 'lido')
    list_filter = ('lido', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    ordering = ('-data_envio',)
    
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order", "is_active")
    list_editable = ("order", "is_active")
    search_fields = ("name", "slug")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "icon", "order", "is_active")
    list_filter = ("category", "is_active", "icon")
    list_editable = ("order", "is_active")
    search_fields = ("title", "description")



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("thumb", "nome", "cargo", "is_active", "ordem")
    list_editable = ("is_active", "ordem")
    search_fields = ("nome", "cargo", "registro", "tags")
    list_filter = ("is_active", "cargo")
    ordering = ("ordem", "nome")

    readonly_fields = ("slug",)

    def thumb(self, obj):
        if obj.foto:
            try:
                src = obj.foto.thumb.url
            except Exception:
                src = obj.foto.url
        else:
            src = static("images/team/placeholder.webp")

        return format_html(
            "<img src='{}' style='width:40px;height:40px;object-fit:cover;border-radius:12px;border:1px solid #ddd' />",
            src,
        )

    thumb.short_description = "Foto"

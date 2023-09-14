from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from museum_api.models import ArtType, Exhibit, Gallery, Position, User, Tour, Article, Review

admin.site.register(ArtType)
admin.site.register(Exhibit)
admin.site.register(Gallery)
admin.site.register(Position)
admin.site.register(Tour)
admin.site.register(Article)
admin.site.register(Review)


class UserAdmin(DefaultUserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "birth_date", "phone_number")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone_number", "birth_date")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "phone_number", "birth_date")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )


admin.site.register(User, UserAdmin)

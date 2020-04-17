from django.contrib import admin

from .models import Post


class ActionPublish:
    """Action для публикации и снятия с публикации"""

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        rows_updated = queryset.update(published=False)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        """Опубликовать"""
        rows_updated = queryset.update(published=True)
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as published." % message_bit)

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)


class PostAdmin(admin.ModelAdmin, ActionPublish):
    """Статьи"""
    list_display = ('title', 'slug', 'created_date', "published", "id")
    list_filter = ("created_date", "published")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    actions = ['unpublish', 'publish']


admin.site.register(Post, PostAdmin)

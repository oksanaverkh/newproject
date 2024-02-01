from django.contrib import admin
from . models import Coin, Author, Post


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'birthday']
    ordering = ['name', '-birthday']
    list_filter = ['name', 'birthday']
    search_fields = ['name']
    search_help_text = 'Поиск по полю имя автора'

    readonly_fields = ['birthday']

    fieldsets = [
        (
            'Author',
            {
                'classes': ['wide'],
                'fields': ['name', 'last_name'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Биография автора',
                'fields': ['birthday', 'biography'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Контактная информация',
                'fields': ['email'],
            }
        ),
    ]


class PostAdmin(admin.ModelAdmin):

    @admin.action(description="Стереть содержание статьи")
    def reset_content(modeladmin, request, queryset):
        queryset.update(content='')

    list_display = ['title', 'content', 'author']
    ordering = ['title', 'author']
    list_filter = ['title', 'author']
    search_fields = ['title']
    search_help_text = 'Поиск по полю заголовок'
    actions = [reset_content]

    readonly_fields = ['is_published']

    fieldsets = [
        (
            'Post',
            {
                'classes': ['wide'],
                'fields': ['title', 'content'],
            },
        ),
        (
            'Details',
            {
                'classes': ['collapse'],
                'description': 'Aвтор',
                'fields': ['author'],
            },
        ),
        (
            'Other info',
            {
                'description': 'Прочая информация',
                'fields': ['is_published', 'views'],
            }
        ),
    ]


admin.site.register(Coin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)

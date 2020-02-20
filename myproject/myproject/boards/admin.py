from django.contrib import admin
from .models import Review, Artist, Content, Genre, Label, Author

admin.site.register(Review)
admin.site.register(Artist)
admin.site.register(Content)
admin.site.register(Genre)
admin.site.register(Label)
admin.site.register(Author)
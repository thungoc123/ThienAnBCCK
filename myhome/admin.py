from django.contrib import admin
from .models import Post,Galery,Comment

# from .models import Comment
# from .models import Author
# from .models import Topic

# Register your models here.
admin.site.register(Post)
admin.site.register(Galery)
admin.site.register(Comment)
# admin.site.register(Author)
# admin.site.register(Topic)
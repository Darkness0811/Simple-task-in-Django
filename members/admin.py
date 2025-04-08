from django.contrib import admin
from .models import Member, Rectangle

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

class RectangleAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'width')
    
    
admin.site.register(Member, MemberAdmin)
admin.site.register(Rectangle,RectangleAdmin)
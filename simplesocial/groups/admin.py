from django.contrib import admin
from . import models

# Register your models here.


class GroupMemberInline(admin.TabularInline):
    # 26
    model = models.GroupMember


admin.site.register(models.Group)

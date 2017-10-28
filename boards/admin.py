# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Board
from .models import Post

# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["name","timestamp"]
	list_display_links = ["name"]
	list_filter = ["timestamp"]
	search_fields = ["name"]
	# list_editable = [""]
	class Meta : 
		model = Board

#admin.site.register(Board,PostModelAdmin)
 
admin.site.register(Board,PostModelAdmin)





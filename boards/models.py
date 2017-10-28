# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User


from django.db import models

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	username = models.CharField(max_length=100,default='admin')
	password = models.CharField(max_length=100,default='Admin@123')


	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board,related_name='topics')
	starter = models.ForeignKey(User, related_name='topics')

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic, related_name = 'posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.ForeignKey(User,null=True,related_name = '+')
	created_by = models.ForeignKey(User, related_name='posts')
    #updated_by = models.ForeignKey(User,null=True)

    	def __str__(self):
    		return self.message

    	def __unicode__(self):
    		return self.message



    
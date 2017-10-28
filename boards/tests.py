# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.urls import resolve
from .views import home
from .models import Board
from .views import home, board_topics


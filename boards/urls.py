from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    
    url(r'^admin/', admin.site.urls),

    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),

    url(r'^dashboard/',views.dashboard, name = 'dashboard'),

    url(r'^index/',views.index, name = 'index'),

    url(r'^calendar/',views.calendar, name = 'calendar'),

    url(r'^supremecourtdetails/$',views.supreme_details, name = 'supreme_details'),

    url(r'^highcourtdetails/$',views.highcourtdetails, name = 'highcourtdetails'),

    url(r'^districtcourtdetails/$',views.districtcourtdetails, name = 'districtcourtdetails'),

	url(r'^login/$',views.login, name = 'login'),

	url(r'^forgotpassword/$',views.forgotpassword, name = 'forgotpassword'),

	url(r'^change_password/$',views.change_password, name = 'change_password'),

	url(r'^registeration/$',views.registeration, name = 'registeration'),

    url(r'^logout/$',views.logout, name = 'logout'),

    url(r'^welcome_email/$',views.welcome_email, name = 'welcome_email'),

    url(r'^landing_page/$',views.landing_page, name = 'landing_page'),

]

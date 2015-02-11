from django.conf.urls import patterns, include, url
from django.contrib import admin
from base.views import home, login, logout, register_base_info
from baby.views import my_home


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ibtt.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', home),
                       url(r'^login/$', login),
                       url(r'^logout$', logout),
                       url(r'^my_home/$', my_home),
                       url(r'^register_base_info', register_base_info),


)

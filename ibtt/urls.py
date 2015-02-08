from django.conf.urls import patterns, include, url
from django.contrib import admin
from ibtt.views import home, login, logout
from baby.views import my_home


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ibtt.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', home),
                       url(r'^login/$', login),
                       url(r'^my_home/$', my_home),
)

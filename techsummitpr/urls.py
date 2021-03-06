from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pages.views.home', name='home'),
    url(r'^joven/$', 'pages.views.joven', name='joven'),
    url(r'^search/$', 'pages.views.search'),

    url(r'^enrollment/$', 'pages.views.enrollment'),
    url(r'^college/$', 'pages.views.college'),
    url(r'^workforce/$', 'pages.views.workforce'),

    url(r'^contact/$', 'pages.views.contact'),
    # url(r'^techsummitpr/', include('techsummitpr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


from django.conf import settings

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

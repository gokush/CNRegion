from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'(?P<content_type>\w+)/provinces/', 'region.views.provinces', 
        name='provinces'),
    url(r'(?P<content_type>\w+)/cities/(?P<province_id>\d+)/', \
        'region.views.cities', name='cities'),
    url(r'(?P<content_type>\w+)/counties/(?P<city_id>\d+)/', \
        'region.views.counties', name='counties'),
    url(r'(?P<content_type>\w+)/towns/(?P<county_id>\d+)/', \
        'region.views.towns', name='towns'),
    url(r'(?P<content_type>\w+)/villages/(?P<town_id>\d+)/', \
        'region.views.villages', name='villages'),
)

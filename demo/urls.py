from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'demo.views.index', name='demo_index'),
    url(r'^foods$', 'demo.views.foods', name='demo_foods'),
    url(r'^foods/(?P<foodid>\d+)/$', 'demo.views.food_detail', name='demo_food_detail'),
    url(r'^admin/', include(admin.site.urls)),
]

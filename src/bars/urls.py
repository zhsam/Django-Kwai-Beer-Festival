from django.conf.urls import url

from .views import (
    # bars_listview,
    BarListView,
    BarDetailView,
    BarsCreateView
)

urlpatterns = [
    url(r'$', BarListView.as_view(), name='list'),
    url(r'^create/$', BarsCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', BarDetailView.as_view(), name="detail"),
    # url(r'^bars/(?P<bar_id>\w+)$', BarDetailView.as_view()),
    # url(r'^bars/asian/$', AsianFusionBarListView.as_view()),
]

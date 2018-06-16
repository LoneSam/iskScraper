from django.conf.urls import url
from . import views

app_name = 'system'

urlpatterns = [
    #url(r'^summary/(?P<system_id>[a-zA_Z0-9]+)/$', views.system_summary, name='system_summary'),
    url(r'^(?P<system_id>[0-9]+)/item/(?P<item_id>[0-9]+)/sellvol/(?P<sell_vol>[0-9]+)$', views.sell_earn, name='sell_earn'),
    url(r'^(?P<system_id>[0-9]+)/item/(?P<item_id>[0-9]+)/spendisk/(?P<spend_isk>[0-9]+)$', views.buy_price, name='buy_price'),
    url(r'^$', views.index, name = 'index'),    
]


"""
from before
urlpatterns = [
    url(r'^system/', include('system.urls')), 
    url(r'^admin/', admin.site.urls),
    #url(r'^$', views.index), 
]
"""
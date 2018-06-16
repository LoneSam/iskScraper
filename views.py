from django.shortcuts import render
from django.http import HttpResponse
from system.iskraper import skraper


# Create your views here.

"""
def index(request):
   p = ParserXML()
   x = p.parseFromURL('http://api.eve-central.com/api/quicklook?usesystem=30000142')
   #s = Skraper(p.toModels())
   
   s = Skraper(p.toObjects())
   
   buying = 9999999
   selling = 9999999
   
   #x = s.getItemsFromIsk(buying)
   #y = s.getIskForItems(selling)
   
   x = s.getItemsFromIsk_objs(buying)
   y = s.getIskForItems_obs(selling)
   
   str = ''
   str +=  'BUYING with: {} isk <br>'.format(buying)
   str += 'Isk spent: {} <br>'.format(x['isk_spent'])
   str += 'Purchase vol: {} <br><br>'.format( x['purch_vol'])
   
   str += 'SELLING Items:{}<br>'.format(selling)
   str += 'Earned: {}<br>'.format(y['earned'])
   str += 'Items remaining: {} <br>'.format(y['items_remaining'])
   
   return HttpResponse(str)
    

"""

def index(request):
    return 0

def buy_price(request,system_id,item_id,spend_isk):
    data = main_data('buy_price',
                     int(system_id),
                     int(item_id),
                     int(spend_isk))
    
    str = 'BUYING with: {} isk <br>'.format(spend_isk)
    str += 'Purchase vol: {} <br><br>'.format( data['purch_vol'])
    str += 'Isk spent: {} <br>'.format(data['isk_spent'])
    str += 'Avg Price: {} <br>'.format(data['isk_spent']/data['purch_vol'])
    
    return HttpResponse(str)

def sell_earn(request,system_id,item_id,sell_vol):
    
    
    return HttpResponse(str)

"""
def system_summary(request):
    return HttpResponse('hello world Sys summry')
"""
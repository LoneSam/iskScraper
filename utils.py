import urllib.parse, urllib.request         
import xml.etree.ElementTree as ET 
from django.utils.dateparse import parse_datetime   
from datetime import datetime    
from .models import Instance, Order
                                           
class ParserXML:
    'Parsing,printing,storing Quicklook data from EVE-market URL queries'

    def __init__(self):
        self.instance_data = {}
        self.orderModels = None
        self.orderModels = []
   
    def parseFromURL(self,url):
        response = urllib.request.urlopen(url)
        xmlIn = response.read()
        xml = xmlIn.decode('ascii',errors='backslashreplace')
        
        root = ET.fromstring(xml)
       
        dataOverview = []
        dataSell = []
        dataBuy = []
        
        for elem in root:
            if elem.tag == 'evec_api':
                listXML(root.getchildren())
                
            elif elem.tag == 'quicklook':
                for data in elem.getchildren():
                    dataOverview.append(data.text)
                    
                    if data.tag == 'sell_orders':
                        for order in data.getchildren():
                            orderData = [order.get('id')]
                            for orderLine in order.getchildren():
                                orderData.append(orderLine.text)
                            dataSell.append(orderData)
                    
                    elif data.tag == 'buy_orders':
                        for order in data.getchildren():
                            orderData = [order.get('id')]
                            for orderLine in order.getchildren():
                                orderData.append(orderLine.text)
                            dataBuy.append(orderData)
                            
            elif elem.tag == 'from' or elem.tag == 'to':
                dataOverview.append(elem.text)
                
        self.instance_data['summary'] = dataOverview
        self.instance_data['sell_orders'] = dataSell
        self.instance_data['buy_orders'] = dataBuy
        
        return self.instance_data
        
    def toModels(self):
        values = self.instance_data['summary']
        instance = Instance(
                    item_id = values[0],
                    itemname = values[1],
                    regions = values[2],
                    hours = values[3],
                    minqty = values[4]
                   )
        instance.save()
              
        
        #Separate buy/sell b/c of 'is_sell' attribute
       
        for order in self.instance_data['sell_orders']:
            o = Order(
                    instance = instance,
                    order = order[0],
                    region_id = order[1],
                    station_id = order[2],
                    station_name = order[3],
                    security = float(order[4]),
                    range = order[5],
                    price = order[6],
                    vol_remaining = order[7],
                    min_volume = order[8],
                    expires = order[9],
                    reported_time = 
                        str(datetime.now().year)+'-'+order[10],
                    is_sell = True
            )
            o.save()
            
        for order in self.instance_data['buy_orders']:
            o = Order(
                      instance = instance,
                      order = order[0],
                      region_id = order[1],
                      station_id = order[2],
                      station_name = order[3],
                      security = float(order[4]),
                      range = order[5],
                      price = order[6],
                      vol_remaining = order[7],
                      min_volume = order[8],
                      expires = order[9],
                      reported_time = 
                        str(datetime.now().year)+'-'+order[10],
                      is_sell = False
                )
            o.save()
        return instance.pk

    def toObjects(self):
        this.instance_obj = Instance(instance_data['summary'])
        
        this.sell_order_objs = []
        for order in self.instance_data['sell_orders']:
            this.sell_order_objs.append(Order('sell',order))
        
        this.buy_order_objs = []
        for order in self.instance_data['buy_orders']:
            this.buy_order_objs.append(Order('buy',order))
            
        return 1
            
class Skraper:
    'Creates system summaries from Order models'
    
    def __init__(self,instance_id):
        self.instance = Instance.objects.filter(pk=instance_id)
        self.s_orders = Order.objects.filter(instance_id=instance_id).filter(is_sell=True)
        self.b_orders = Order.objects.filter(instance_id=instance_id).filter(is_sell=False)
    
    
    
    def getItemsFromIsk(self,avail_isk):
        o_price_asc = self.s_orders.order_by('price')        

        purch_vol = 0
        
        for o in o_price_asc:
            buyable_vol = avail_isk/o.price
            
            if buyable_vol < 1:
                break
            
            elif buyable_vol >= o.vol_remaining:
                avail_isk -= o.price * o.vol_remaining
                purch_vol += o.vol_remaining
                
            else:
                avail_isk -= o.price * int(buyable_vol)            
                purch_vol += int(buyable_vol)
        return {'isk_left' : avail_isk, 'purch_vol' : purch_vol}
    
    def getIskForItems(self,avail_items):
        o_price_dsc = self.b_orders.order_by('-price')
        
        earned = 0
        
        for o in o_price_dsc:
            if avail_items <= 0:
                break
            elif o.vol_remaining <= avail_items:
                avail_items -= o.vol_remaining
                earned += o.vol_remaing * o.price
            elif o.vol_remaining > 0:
                earned += o.price * avail_items
                avail_items = 0 
        
        return {'earned' : earned, 'items_remaining' : avail_items}
    
    def getItemsFromIsk_objs(self,avail_isk):
        o_price_asc = self.sell_order_objs.sort(key=lambda x: x.price)   

        purch_vol = 0
        
        for o in o_price_asc:
            buyable_vol = avail_isk/o.price
            
            if buyable_vol < 1:
                break
            
            elif buyable_vol >= o.vol_remaining:
                avail_isk -= o.price * o.vol_remaining
                purch_vol += o.vol_remaining
                
            else:
                avail_isk -= o.price * int(buyable_vol)            
                purch_vol += int(buyable_vol)
                
        return {'isk_left' : avail_isk, 'purch_vol' : purch_vol}
    
    def getIskForItems_objs(self,avail_items):
        o_price_dsc = self.buy_order_objs.sor(key=lambda x: x.price, reverse=True)
        
        earned = 0
        
        for o in o_price_dsc:
            if avail_items <= 0:
                break
            elif o.vol_remaining <= avail_items:
                avail_items -= o.vol_remaining
                earned += o.vol_remaing * o.price
            elif o.vol_remaining > 0:
                earned += o.price * avail_items
                avail_items = 0 
        
        return {'earned' : earned, 'items_remaining' : avail_items}
    
    
    
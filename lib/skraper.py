import urllib.request
import xml.etree.ElementTree as ET
from .skrapers import *

#there may be a better url

# Turn Parsed Quicklook data to summary-object or order-objects list        
def data2Objs(data_dict,section_name):
    if section_name == 'summary':
        r = Instance(data_dict['summary'])
    elif section_name == 'sell_orders' or section_name == 'buy_orders':
        r = []
        for order_vals in data_dict[section_name]:
            r.append(Order(order_vals))
    else:
        raise ValueError("Expected 'data_dict' key - received:",section_name)
        
    return r

# Return purchase data given the amount of isk user is willing to spend on item
def buyItems(avail_isk,sell_orders):
    sell_orders.sort(key=lambda x: x.price)   
    
    if not avail_isk: avail_isk = float('inf')
    
    summarizer = OrderSummarizer()
    
    for o in sell_orders:
        avail_isk -= o.price*o.vol_remaining
        if avail_isk <= 0:
            unpurchased = int((avail_isk*-1)/o.price+0.999)
            summarizer.addOrder(o,unpurchased)
            break
        else:
            summarizer.addOrder(o)
        
    return summarizer

# Return sell data given the # items the user wants to sell
def sellItems(avail_items,buy_orders):
    buy_orders.sort(key=lambda x: x.price, reverse=True)
    
    if not avail_items: avail_items = float('inf')
    
    summarizer = OrderSummarizer()
    
    for o in buy_orders:
        avail_items -= o.vol_remaining
        if avail_items <= 0:
            unpurchased = avail_items*-1
            summarizer.addOrder(o,unpurchased)
            break
        else:
            summarizer.addOrder(o)
    
    return summarizer

# Not the most efficient...
def parseQuicklookFromURL(url):
    with urllib.request.urlopen(url) as response:
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
    
    instance_data = {}      
    instance_data['summary'] = dataOverview
    instance_data['sell_orders'] = dataSell
    instance_data['buy_orders'] = dataBuy
    
    return instance_data


def buy_data(system_id,item_id,avail_isk):
    url = 'http://api.eve-central.com/api/quicklook/onpath/from/{}/to/{}/fortype/{}'
    custom_url = url.format(system_id,'Jita',item_id)
    parsed_data = parseQuicklookFromURL(custom_url)
    sell_orders = data2Objs(parsed_data,'sell_orders')
    summarizer = buyItems(avail_isk,sell_orders)
    summarizer.addSystem(system_id)
    return summarizer

def sell_data(system_id,item_id,avail_items):
    url = 'http://api.eve-central.com/api/quicklook/onpath/from/{}/to/{}/fortype/{}'
    custom_url = url.format(system_id,'Jita',item_id)
    parsed_data = parseQuicklookFromURL(custom_url)
    buy_orders = data2Objs(parsed_data,'buy_orders')
    summarizer = sellItems(avail_items,buy_orders)
    summarizer.addSystem(system_id)
    return summarizer





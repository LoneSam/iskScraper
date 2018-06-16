from skraper import *
from models import *
from scrapies import *
from skrapers import *
from time import sleep

#CALL THE GLOBAL INIT

def update_instance_cache(instance_id = None):
    if system_id:
        Instance(id=instance_id).delete()
    """
    should automatically delete CASCADE delete
    
    """
    
    
def clean_system_cache():
    """
    if it's older than kill system cache
    """
    (kill_system_cache)
    for s in delete_systems:
        System.removeFromDB()
    

def system_looper(system_ids,item_id,seconds):
   # system_ids = ['Amarr','Dodixie']
    
   # avail_isk = 100000000
   # avail_items = 20000000
    """
    for s in system_ids:
        bs = buy_data(s,34,avail_isk)
        ss = sell_data(s,34,avail_items)
        print(s+'-',)
        print('Available isk: ',avail_isk)
        print(bs)
        print(s+'-',)
        print('Available items: ',avail_items)
        print(ss)
        print('')
        
    """
    
    time.sleep(global cache_update_tim)
    #return sys_summarizers
    
def start():
    system_looper()
class Instance:
    'System-Item Query Instance'
    def __init__(self,instance_vals):        
        self.item_id = instance_vals[0]
        self.itemname = instance_vals[1]
        self.regions = instance_vals[2]
        self.hours = instance_vals[3]
        self.minqty = instance_vals[4]

class Order:
    'buy/sell station order'
    
    def __init__(self,order_vals,type = None):
        #self.instance = instance
        self.order = order_vals[0]
        self.region_id = order_vals[1]
        self.station_id = order_vals[2]
        self.station_name = order_vals[3]
        self.security = float(order_vals[4])
        self.range = order_vals[5]
        self.price = float(order_vals[6])
        self.vol_remaining = int(order_vals[7])
        self.min_volume = int(order_vals[8])
        self.expires = datetime.strptime(order_vals[9],'%Y-%m-%d')
        self.reported_time = datetime.strptime(str(datetime.now().year)+'-'+
                order_vals[10],'%Y-%m-%d %H:%M:%S') 
        self.type = type

class System:
    def __init__(self,system):
        if system.isdigit():
            self.system_id = system
            self.system_name = self.getSystemName()
        else:
            self.system_name = system
            self.system_id = self.getSystemID()
    
    def getSystemName(self,system = self.system_id):
        if self.system_name == system or self.system_name:
            return self.system_name
        else:
            """
            go to db: select system_name where system_id = self.system_id
            """
            if not data_is_returned:
                raise ValueError('Could not find {} in the database'.format(system))
            return = self.system_name
            
    def getSystemID(self,system = self.system_name):
        if self.system_id:
            return self.system_id
        else:
            """
            go to db: select system_name where system_id = self.system_id
            """
        

def Item:
    def __init__(self,item):
        if item.isdigit():
            self.item_id = item
            self.item_name = self.getItemName()
        else:
            self.item_name = item
            self.item_id = self.getItemID()
    
    def getItemName(self,item = self.item_id):
        if self.item_name == item or self.item_name:
            return self.item_name
        else:
            """
            go to db: select item_name where item_id = self.item_id
            """
            if not data_is_returned:
                raise ValueError("DBError: Could not find '{}' in the database.".format(item))
            return = self.item_name
            
    def getItemID(self,item = self.item_name):
        if self.item_id:
            return self.item_id
        else:
            """
            go to db: select item_name where item_id = self.item_id
            """
class CompareSystems:
    def __init__(self,system_id1,system_id2):
        self.jumpsAway = self.getJumpsAway()
        
    def getJumpsAway(self):
        pass
    
class OrderSummarizer:
    'get summary of list of All Orders or list of Buyables or Sellables'
    
    def __init__(self, system_id = '99999999'):
        self.orders = []
        self.system_id = system_id
        
    def update(self):
        self.count = self.count()
        self.max = self.max()
        self.min = self.min()
        self.median = self.median()
        self.volume = self.volume()
        self.value = self.value()
        self.receipts = self.receipts()
        self.expiringSoonest = self.expiringSoonest()
        self.oldestUpdate = self.oldestUpdate()
        
    def saveToDB(self):
        pass
    
    def addOrder(self,order,unpurchased = None):
        if unpurchased:
            order.vol_remaining -= unpurchased
        self.orders.append(order)
    
    def addSystemID(self,system_id):
        if not system_id.isdigits():
            raise ValueError('System_id requires numbers, recieved:',system_id)
        elif self.system:
            raise ValueError('System already specified for',self)
        else:
            self.system = system_id
    
    def toXML(self):
        pass
        
    def getDict(self):
        self.update()
        return self.__dict__

    def count(self):
        return len(self.orders)
    
    def max(self):
        return max(o.price for o in self.orders)
    
    def min(self):
        return min(o.price for o in self.orders)
    
    def median(self):
        mid_vol = self.volume()/2
        for o in self.orders:
            mid_vol -= o.vol_remaining
            if mid_vol <= 0:
                median = o.price
                break
        return median
    
    def volume(self):
        return sum(o.vol_remaining for o in self.orders)
    
    def value(self):
        return sum(o.price*o.vol_remaining for o in self.orders)

    def receipts(self):
        return [(o.order,o.price,o.vol_remaining,o.price*o.vol_remaining) for o in self.orders]
    
    def expiringSoonest(self):
        return str(max(o.expires for o in self.orders))
        
    def oldestUpdate(self):
        return str(min(o.reported_time for o in self.orders))
    
    def __str__(self): 
        str = 'count: {}'.format(self.count())
        str += '\nmax: {}'.format(self.max())
        str += '\nmin: {}'.format(self.min())
        str += '\nmedian: {}'.format(self.median())
        str += '\nvolume: {}'.format(self.volume())
        str += '\nvalue: {}'.format(self.value())
        #str += '\nreceipts: (call self.receipts())'
        str += '\nexpiringSoonest: {}'.format(self.expiringSoonest())
        str += '\noldestUpdate: {}'.format(self.oldestUpdate())
        return str
    
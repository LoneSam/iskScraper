from django.db import models

# Create your models here.

class Instance(models.Model):
    item_id   = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)
    itemname  = models.CharField(max_length=256,null=True)
    regions   = models.CharField(max_length=256,null=True)
    hours     = models.PositiveIntegerField()
    minqty    = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return str(self.pk)
    
class Order(models.Model):
    instance      = models.ForeignKey(Instance, on_delete=models.CASCADE)
    order         = models.PositiveIntegerField()
    region_id     = models.PositiveIntegerField()
    station_id    = models.PositiveIntegerField()
    station_name  = models.CharField(max_length=256)
    security      = models.FloatField()
    range         = models.PositiveIntegerField()
    price         = models.DecimalField(max_digits=11,decimal_places=2)
    vol_remaining = models.PositiveIntegerField()
    min_volume    = models.PositiveIntegerField()
    expires       = models.DateField()
    reported_time = models.DateTimeField()  #12-29 16:56:28
    is_sell       = models.BooleanField()
    
    def __str__(self):
        return str(self.instance) +' => '+ str(self.order)
        


class Summary(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    system_id = models.PositiveIntegerField()
    order_sample_size = models.PositiveIntegerField()
    max_price =  models.DecimalField(max_digits=15,decimal_places=2)
    min_price =  models.DecimalField(max_digits=15,decimal_places=2)
    median_price = models.DecimalField(max_digits=15,decimal_places=2)
    total_volume = models.PositiveIntegerField()
    total_value = models.PositiveIntegerField()
    #receipts = 
    expiring_soonest = models.DateField()
    oldest_update = models.DateTimeField()
    
    
class Item(models.Model):
    # Get straight from db
    pass


class System2Station(models.Model):
    solarsystem_id = models.PositiveIntegerField()
    region_id = models.PositiveIntegerField()
    region_name = models.CharField(max_length=256)
    solarsystem_name = models.CharField(max_length=256)
    security = models.FloatField()
    
    
    #delete these after import
    x = models.CharField(max_length=256)
    y = models.CharField(max_length=256)
    z = models.CharField(max_length=256)
    flat_x = models.CharField(max_length=256)
    flat_y = models.CharField(max_length=256)
    dotlan_x = models.CharField(max_length=256)
    dotlan_y = models.CharField(max_length=256)
    has_station = models.CharField(max_length=256)
    #delete above

class Station(models.Model):
    station_id = models.CharField(max_length=11)
    solarsystem_id = models.CharField(max_length=11)
    solarsystem_name = models.CharField(max_length=256)
    region_id = models.CharField(max_length=11)
    region_name = models.CharField(max_length=256)
    station_type_id = models.CharField(max_length=11)
    station_name = models.CharField(max_length=256)
    corporation_id = models.CharField(max_length=11)
    corporation_name = models.CharField(max_length=256)
    created = models.DateTimeField()
    updated = models.DateTimeField()

class FromToSystem(models.Model):
    from_solarsystem_id = models.PositiveIntegerField() 
    to_solarsystem_id = models.PositiveIntegerField()
    from_region_id = models.PositiveIntegerField()
    to_region_id = models.PositiveIntegerField()

class CountedHopsOnRoute(models.Model):
    from_solarsystem_id = models.CharField(max_length=11)
    to_solarsystem_id = models.CharField(max_length=11)
    jumps = models.PositiveIntegerField()

#one of the steps on a route to somewhere
#optional
class SystemIDOnRoute():
    from_solarsystem_id = models.CharField(max_length=11)
    to_solarsystem_id = models.CharField(max_length=11)
    jump_step_number = models.PositiveIntegerField()
    hop_solarsystem_id = models.CharField(max_length=11)




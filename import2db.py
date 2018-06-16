from django.db import models
from models import FromToSystem

filename = 'jumps.csv'

with open(filename,"r") as f:
    csv = f.read()

values = []
for l in csv:
    values.append(l.split(','))
 
count = 0   
for l in values:
    m = FromToSystem(
        from_solarsystem_id = l[0],
        to_solarsystem_id = l[1],
        from_region_id = l[2],
        to_region_id = l[3]
    )
    m.save()
    count += 1
    print(count,"saved to db")
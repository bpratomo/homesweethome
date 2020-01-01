import pandas as pd 

from browse.models import Home

qs = Home.objects.all()

df = read_frame(qs)

print(df)
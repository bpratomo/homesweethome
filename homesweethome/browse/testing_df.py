import pandas as pd  
from sqlalchemy import create_engine


# Create sqlalchemy connection 
engine = create_engine('postgresql://postgres:Teknikfisika123@localhost/homesweethome')

df = pd.read_sql('browse_home',engine)
print(df.loc[23])
import numpy as np
import pandas as pd 
# E-commerce product catalogue 
data = {
    'product_id': [101,102,103,104,105],
    'product_name': ['Wireless headphone','Keyboard', 'Mouse','Smart Watch', 'Speaker'],
    'category': ['Electronics','Electronics','Accessories','Electronics','Accessories'],
    'cart': ['1001','1001','1001','1001','1001'],
    'shipping' : [50.0,40.0,60.0,45.0,50.0]}
df=pd.DataFrame(data)
print("Original Product Catalog")
print(df)


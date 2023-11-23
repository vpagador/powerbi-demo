import pandas as pd
import numpy as np
import random
import uuid
from datetime import datetime, timedelta

    
def create_products(num_of_products:int):
    product_ids = [str(uuid.uuid4()) for products in range(0,num_of_products)]
    prices = np.random.randint(1,6,size=num_of_products)+0.99
    weights = np.random.randint(1,20,size=num_of_products)
    unit_weights = [str(weight) + 'kg' for weight in weights]
    new_dictionary = {'product_id': product_ids,
                        'sale_price' : prices,
                        'weight': unit_weights}
    product_df = pd.DataFrame(new_dictionary)
    return product_df
    

df = create_products(6)
df.to_csv('dim_products.csv')



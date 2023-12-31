import pandas as pd
import numpy as np
import random
import shortuuid
from datetime import datetime, timedelta


class FactTableGenerator:

    def __init__(self, num_of_rows, product_file):
        self.num_of_rows = num_of_rows
        self.product_file = product_file
        np.random.seed(42)

    def _fact_id_column(self) -> dict:
        fact_ids = [str(shortuuid.uuid()) for products in range(0,self.num_of_rows)]
        column_dict = {'order_id': fact_ids}
        return column_dict

    def _customer_id_column(self,num_of_customers:int) -> dict:
        customer_ids = np.random.randint(1,
                          num_of_customers,
                          size=self.num_of_rows)
        column_dict = {'customer_id': list(customer_ids)}
        return column_dict
    

    def _date_id_column(self,start_date:str, end_date:str) -> dict:
        start_datetime = datetime(year=int(start_date[0:4]),     # year 
                                  month=int(start_date[4:6]),     # month
                                  day=int(start_date[6:8]))     # day
        end_datetime = datetime(year=int(end_date[0:4]), 
                                month=int(end_date[4:6]), 
                                day=int(end_date[6:8]))

        # Calculate the range of days between start and end date
        days_range = (end_datetime - start_datetime).days

        # Generate random datetime values within the range
        random_dates = [start_datetime + timedelta(days=random.randint(0, days_range)) for _ in range(self.num_of_rows)]
        date_dict =  {'date_id': random_dates}
        return date_dict
    
    def _product_columns(self, dim_product_filepath) -> dict:
        df = pd.read_csv(dim_product_filepath)
        chosen_products = [random.choice(list(zip(df['product_id'],df['sale_price']))) for id in range(0,self.num_of_rows)]
        quantities = self._product_quantity_column()
        ids = [product[0] for product in chosen_products]
        sales = [product[1]*quant for product,quant in zip(chosen_products,quantities)]
        column_dict = {'product_id': ids,
                        'sales':sales,
                        'quantities':quantities}
        df = pd.DataFrame(column_dict)
        return df
    
    def _product_quantity_column(self) -> list:
        quantities = [num for num in range(1,20)]
        product_quantity = [random.choice(quantities) for _ in range(self.num_of_rows)]
        return product_quantity
    
    def _combine_columns(self,list_of_dicts : dict) -> pd.DataFrame:
        combined_dict = {}
        for dictionary in list_of_dicts:
            combined_dict.update(dictionary) 
        combined_dataframe = pd.DataFrame(combined_dict)
        return combined_dataframe
    
    def fact_table_generator(self):
        dates = self._date_id_column('20230101','20231201')
        facts = self._fact_id_column()
        products = self._product_columns(self.product_file)
        customers = self._customer_id_column(40)
    
        df = self._combine_columns([facts,dates,products,customers,products])
        return df

if __name__ == '__main__':
    generator = FactTableGenerator(100, 'data_files/dim_products.csv')
    df = generator.fact_table_generator()
    print(df)
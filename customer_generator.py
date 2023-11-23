import pandas as pd
import random

class CustomerGenerator:
    
    def __init__(self, file):
        self.df = pd.read_csv(file)

    def _phone_generator(self, unique_values):
        phone_numbers = []
        for i in range(len(unique_values)):
            phone_number = "(+38)"
            # the for loop is used to append the other 9 numbers. 
            # the other 9 numbers can be in the range of 0 to 9. 
            for i in range(1, 10): 
                phone_number += str(random.randint(0, 9)) 
            phone_numbers.append(phone_number)
        return phone_numbers

    def derive_customers(self, customer_id_column:str):
        id_column = self.df[customer_id_column]
        unique_values = set(id_column)
        phone_numbers = self._phone_generator(unique_values)
        # Random region assignment
        regions = [random.choice(['North', 'South', 'East', 'West']) for _ in range(len(unique_values))]
        new_dictionary = {customer_id_column : list(unique_values),
                          "phone_number": phone_numbers,
                          'Region': regions}
        customer_df = pd.DataFrame(new_dictionary)
        return customer_df
    
        
    
customer_generator = CustomerGenerator('fact_table.csv')
df = customer_generator.derive_customers('customer_id')
df.to_csv('dim_customers.csv')



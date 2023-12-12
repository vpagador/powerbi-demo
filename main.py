from customer_generator import CustomerGenerator
from fact_table_generator import FactTableGenerator
from product_generator import create_products

if __name__ == '__main__':
    # Create first the product table
    product_df = create_products(6)
    product_df.to_csv('data_files/dim_products.csv')
    # Create fact table, with sales data derived from products csv created
    generator = FactTableGenerator(200, 'data_files/dim_products.csv')
    facts_df = generator.fact_table_generator()
    facts_df.to_csv('data_files/fact_table.csv')
    # Create customer table, derived from facts table
    customer_generator = CustomerGenerator('data_files/fact_table.csv')
    df = customer_generator.derive_customers('customer_id')
    df.to_csv('data_files/dim_customers.csv')
    print('done')

from customer_generator import CustomerGenerator
from fact_table_generator import fact_table_generator
from product_generator import create_products

if __name__ == '__main__':
    # Create first the product table
    product_df = create_products(6)
    product_df.to_csv('dim_products.csv')
    # Create fact table, with sales data derived from products csv created
    facts_df = fact_table_generator(200)
    facts_df.to_csv('fact_table.csv')
    # Create customer table, derived from facts table
    customer_generator = CustomerGenerator('fact_table.csv')
    df = customer_generator.derive_customers('customer_id')
    df.to_csv('dim_customers.csv')
    print('done')
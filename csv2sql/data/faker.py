import pandas as pd
import random
from faker import Faker

fake = Faker()

def generate_customers(num=150):
    data = []
    for i in range(1, num + 1):
        data.append({
            'id': i,
            'name': fake.name(),
            'email': fake.email().lower(),
            'country': fake.country()
        })
    return pd.DataFrame(data)

def generate_sales(num=200, customer_count=150):
    products = ['Notebook', 'Pencil', 'Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Desk Chair']
    data = []
    for i in range(1, num + 1):
        data.append({
            'sale_id': i,
            'customer_id': random.randint(1, customer_count),
            'product': random.choice(products),
            'amount': round(random.uniform(5.0, 1500.0), 2),
            'sale_date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    customers_df = generate_customers(150)
    sales_df = generate_sales(200, 150)

    customers_df.to_csv('data/customers.csv', index=False)
    sales_df.to_csv('data/sales.csv', index=False)
    
    print("Generated customers.csv and sales.csv with large data!")

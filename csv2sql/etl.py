import pandas as pd
import pyodbc
from config import DB_CONFIG
from sys import argv
from dotenv import dotenv_values

config = dotenv_values()

def get_connection():
    if len(argv) == 2:
        if argv[1] == "docker":
            print("Docker mode")
            conn_str = (
                f"DRIVER={{{DB_CONFIG['driver']}}};"
                f"SERVER=localhost,1433;"
                f"DATABASE={DB_CONFIG['database']};"
                f"UID=SA;"
                f"PWD={config.get("MS_PASSWORD")};"
            )
        else:
            print("Unknown argument")
            exit(1)
    
    else:
        conn_str = (
            f"DRIVER={{{DB_CONFIG['driver']}}};"
            f"SERVER={DB_CONFIG['server']};"
            f"DATABASE={DB_CONFIG['database']};"
            f"Trusted_Connection={DB_CONFIG['trusted_connection']};"
        )
    
    return pyodbc.connect(conn_str)

def load_to_sql(df, table_name, conn):
    cursor = conn.cursor()
    columns = ','.join(df.columns)
    placeholders = ','.join(['?'] * len(df.columns))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        try:
            cursor.execute(query, tuple(row))
        except Exception as e:
            print(f"Error inserting row {row} into {table_name}: {e}")

    conn.commit()
    cursor.close()

def clean_customers(df):
    df.dropna(inplace=True)
    df['email'] = df['email'].str.lower()
    return df

def run_etl():
    try:
        conn = get_connection()

        # Extract & Transform customers
        df_customers = pd.read_csv('data/customers.csv')
        df_customers = clean_customers(df_customers)
        load_to_sql(df_customers, 'customers', conn)

        # Extract & Transform sales
        df_sales = pd.read_csv('data/sales.csv')
        df_sales.dropna(inplace=True)
        load_to_sql(df_sales, 'sales', conn)

        conn.close()
        print(" ETL completed successfully.")

    except Exception as e:
        print(" ETL failed:", e)

if __name__ == "__main__":
    run_etl()

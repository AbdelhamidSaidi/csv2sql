# CSV to SQL Server ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-2022-blue?logo=microsoftsqlserver&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-1.5+-blue)
![pyodbc](https://img.shields.io/badge/pyodbc-4.0+-green)

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline that reads data from CSV files, cleans and transforms it using Python, and loads it into a SQL Server database.

---

## Features

- Extract data from CSV files (`customers.csv` and `sales.csv`)
- Transform data by cleaning null values and normalizing email addresses
- Load data into SQL Server tables (`customers` and `sales`)
- Uses Windows Authentication for secure database connection
- Easily extensible and automatable

---

## Prerequisites

- Python 3.7 or higher
- SQL Server instance with access rights
- Python packages listed in `requirements.txt`
- ODBC Driver 17 for SQL Server installed
- (Optional) SQL Server Management Studio (SSMS) for managing your database

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/csv-to-sqlserver-etl.git
cd csv-to-sqlserver-etl
```



### 2. Create SQL Server Database and Tables

Connect to your SQL Server and run the following SQL commands to set up the database and tables:

```sql
CREATE DATABASE etl_demo;
GO
USE etl_demo;

CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(100),
    amount FLOAT,
    sale_date DATE
);
```

### 3. Prepare CSV Data

Place your CSV files in the `data/` directory:

* `data/customers.csv`
* `data/sales.csv`

Example CSV content is provided in the repository.

### 4. Configure Database Connection

Edit the `config.py` file to match your SQL Server connection details.

```python
DB_CONFIG = {
    'server': 'YOURSERVERNAME',         
    'database': 'etl_demo',
    'driver': 'ODBC Driver 17 for SQL Server',
    'trusted_connection': 'yes'            
}
```

### 5. Install Python Dependencies

Install required packages using:

```bash
pip install -r requirements.txt
```

### 6. Run the ETL Pipeline

Execute the ETL script:

```bash
python etl.py
```

You should see:

```
 ETL completed successfully.
```

---

## Project Structure

```
csv2sql
      │   config.py
      │   etl.py
      │   requirements.txt
      │   SQLQuery1.sql
      │
      └───data
              │ customers.csv
              └─sales.csv 
```

## Contact

Created by Abdelhamid Saidi
Feel free to reach out with questions or suggestions.

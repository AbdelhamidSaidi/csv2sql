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

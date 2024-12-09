import sqlite3
import pandas as pd

DATABASE = 'data.db'
CSV_DATA_FILE = 'Sample - Superstore.csv'

# Create SQLite database and table
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Load data from CSV file into SQLite database
df = pd.read_csv(CSV_DATA_FILE)
df.to_sql('sales_history', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

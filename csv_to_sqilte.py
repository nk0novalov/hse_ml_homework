import pandas as pd
import sqlite3

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('your_csv_file.csv')

# Connect to a SQLite database (this will create a new database if it doesn't exist)
conn = sqlite3.connect('your_database.db')

# Write the DataFrame to a SQLite table
df.to_sql('your_table_name', conn, index=False, if_exists='replace')

# Close the database connection
conn.close()



import snowflake.connector
import sys
sys.path.append('../FileHandling')
import CSV_Wrapper

# Snowflake account information
account = 'your_account'
username = 'your_username'
password = 'your_password'
warehouse = 'your_warehouse'
database = 'your_database'
schema = 'your_schema'

# Establish a connection to Snowflake
conn = snowflake.connector.connect(
    user=username,
    password=password,
    account=account,
    # warehouse=warehouse,
    database=database,
    schema=schema
)

# Create a cursor object to interact with Snowflake
cursor = conn.cursor()

# Example: Execute a SQL query
cursor.execute("SELECT * FROM RISHABH_ASSIGNMENT LIMIT 100")

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row)

csvHandler = CSV_Wrapper.CSVHandler('data.csv')

csvHandler.overwrite_csv(rows)

# Close the cursor and connection
cursor.close()
conn.close()

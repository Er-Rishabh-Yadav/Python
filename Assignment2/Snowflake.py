import pandas as pd
import snowflake.connector

# Snowflake connection parameters
snowflake_user = 'Rishabh'
snowflake_password = 'Snowflake@6308'
snowflake_account = 'kha80474'
snowflake_database = 'INTERNAL_TRAINING'
snowflake_schema = 'ASSIGNMENT_2'
snowflake_warehouse = 'COMPUTE_WH'
snowflake_table = 'weather_data_table'

# Load CSV data into a DataFrame
csv_filename = r'Assignment2\weather_data.csv'
df = pd.read_csv(csv_filename)

# Create Snowflake connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)

# Create cursor
cur = conn.cursor()

# Insert data into Snowflake table
for index, row in df.iterrows():
    cur.execute(
        f"INSERT INTO {snowflake_table} (date, temperature_2m) VALUES ('{row['date']}', {row['temperature_2m']})"
    )

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data added to Snowflake table.")

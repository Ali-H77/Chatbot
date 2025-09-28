import pandas as pd
import sqlite3
df = pd.read_excel('amazon_product_reviews.xlsx') 
conn = sqlite3.connect('Excel_database.db')
df.to_sql('Customer', conn, if_exists='replace', index=False)
conn.close()

#### **1. Import Database**
"""

# Import file from your system
from google.colab import files
file = files.upload()

"""#### **2. Connect with SQLite Database**"""

# Connect with sqlite database
# Import necessary libraries
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')


import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables
